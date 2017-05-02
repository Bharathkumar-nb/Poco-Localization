from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse,HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.models import User
from .models import Related, Content, Assessment, Module, Course, Video, Student, AssessmentSubmission
from .models import ContentProgress, AssessmentProgress, VideoProgress, CourseProgress, ModuleProgress

from django.utils import timezone
from datetime import datetime
import subprocess
import re
import json
import imp
import ntpath
import os
import sys
import subprocess
from shutil import copyfile
from django.template import RequestContext
from oauth2client import client, crypt
from django.conf import settings
from django.contrib.auth.decorators import login_required

import os
import logging
import httplib2
from django.contrib.auth import login, authenticate
from django.template.defaultfilters import slugify
from django.forms.models import model_to_dict
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.models import Site



class LessonView(generic.DetailView):
    from django.template.defaultfilters import slugify
    template_name = 'main/lesson.html'
    model = User

    """
    Constructor. Called in the URLconf; can contain helpful extra
    keyword arguments, and other things.
    """
    #module_id = self.kwargs.get('module')
    #assessments = Assessment.objects.filter(module_id=module_id)
    #contents = Content.objects.filter(module_id=module_id)
    #relateds = Related.objects.filter(module_id=module_id)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print("REQUEST SESSION", request.session.items())
        print("GET ITEMS: ", context.items())
        print("RESPONSE:", self.render_to_response(context))
        #ADMIN CHECK
        if request.user.is_superuser:
            #return HttpResponseNotFound("<br/><br/><h1 style='text-align:center;vertical_align:middle;'>Signed in as admin, please resign-in to <a href='http://poco.pythonanywhere.com/main/login/'>Poco<a> to access this page</h1>")
            return HttpResponseNotFound("<br/><br/><h1 style='text-align:center;vertical_align:middle;'>Signed in as admin, please resign-in to <a href='http://127.0.0.1:8000/main/login/'>Poco<a> to access this page</h1>")
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LessonView, self).get_context_data(**kwargs)
        module_id = int(self.kwargs.get('module'))
        #print('MODULE_ID ', module_id)
        context['module_obj'] = Module.objects.get(id=module_id)
        context['assessments'] = Assessment.objects.filter(module_id=module_id).order_by('order')
        context['contents'] = Content.objects.filter(module_id=module_id)
        context['videos'] = Video.objects.filter(module_id=module_id)
        context['relateds'] = Related.objects.filter(module_id=module_id)
        print("GET CONTEXT DATA: ", context.items())
        #print("VERSION", sys.version)

        # set up progress data for student if it doesnt exist
        student_instance = context['object'].students
        for content_instance in context['contents']:
            content_prog,created = student_instance.contentprogress_set.get_or_create(content=content_instance)
            #print(content_prog,created)
        for assessment_instance in context['assessments']:
            assessment_prog,created = student_instance.assessmentprogress_set.get_or_create(assessment=assessment_instance)
            #print(assessment_prog,created)
        for video_instance in context['videos']:
            video_prog,created = student_instance.videoprogress_set.get_or_create(video=video_instance)
            #print(video_prog,created)
        return context

    def setupEnv(self, code, envFile, username):
        #directory = '/home/poco/waggle-classroom/main/media/user_{}_tmp_dir'
        #test_filename = '/home/poco/waggle-classroom/main/media/user_{}_tmp_dir/test.py'.format(username)
        #test_filename = '/home/poco/waggle-classroom/main/media/user_{}.py'.format(username)
        test_filename = os.path.join(settings.BASE_DIR, "main", "media", 'user_{}.py'.format(username))
        code_lines = code.splitlines()
        first_line = (code_lines[0]).expandtabs(0)
        if len(code_lines)>1:
            other_lines = code_lines[1:]
            new_code = first_line+ "\n"+'\n'.join(map(lambda s:('\t'+s).expandtabs(8),other_lines)) #lines after first must be indented
        else:
            new_code = first_line
        print("USER CODE AFTER SETUP: {}".format(new_code))
        with open(test_filename, "w") as outfile, open(envFile, 'r', encoding='utf-8') as infile:
            text = infile.read()
            text_with_code = re.sub('&&&', new_code, text,flags=re.M)
            text_with_code = re.sub('# paste user code here', '', text_with_code,flags=re.M)
            outfile.write(text_with_code)
        return test_filename

    def runCode(self, fname):
        try:
            p = subprocess.Popen('python '+fname, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            return p.communicate()  # this gets you pipe values
        except Exception as e:
            return 'error'+e
        else:
            return "else"

    def post(self, request, *args, **kwargs):
        postdata = request.POST.dict()
        print('POST DATA: {}'.format(postdata))
        if(request.POST.get('video_click')):
            videoID = request.POST.get('videoID')
            my_student = Student.objects.get(user=request.user)
            my_video = Video.objects.get(id=int(videoID))
            video_progress = VideoProgress.objects.get(student=my_student, video=my_video)
            video_progress.clicks_on_video_open_counter = video_progress.clicks_on_video_open_counter + 1
            video_progress.save()
            return HttpResponse('django says the video click was recorded')
        elif(request.POST.get('content_click')):
            contentID = request.POST.get('contentID')
            my_student = Student.objects.get(user=request.user)
            my_content = Content.objects.get(id=int(contentID))
            content_progress = ContentProgress.objects.get(student=my_student, content=my_content)
            content_progress.clicks_on_content_tab_counter = content_progress.clicks_on_content_tab_counter + 1
            content_progress.save()
            return HttpResponse('django says the content click was recorded')
        elif(request.POST.get('html_notes')):
            updated_note_table = request.POST.get('html_notes')
            videoID = request.POST.get('videoID')
            video_timepoint = request.POST.get('time')
            print("VIDEOID=%s,\t HTML_NOTES: %s" % (videoID, updated_note_table))
            my_student = Student.objects.get(user=request.user)
            my_video = Video.objects.get(id=int(videoID))
            video_progress = VideoProgress.objects.get(student=my_student, video=my_video)
            video_progress.video_notes = updated_note_table
            video_progress.video_timepoint= video_timepoint
            video_progress.save()
            return HttpResponse('django says the note was saved')
        elif(request.POST.get('submittedcode')):
            usr_code = request.POST.get('submittedcode')
            #if re.search(r'print\(.+\)', usr_code) or re.search(r'plt.show\(.+\)', usr_code):
            if re.search(r'print\(.+\)', usr_code) or re.search(r'plt.show\(.+\)', usr_code):
                #parsed_result_feedback = "Print and show are disabled in assessment submissions. Please practice using these in your notebooks."
                parsed_result_feedback = "Print"
                return HttpResponse(parsed_result_feedback)
            assessmentID = request.POST.get('assessmentID')
            print('USER CODE: {}'.format(usr_code))
            print('ASSESSMENT ID: {}'.format(usr_code, assessmentID))
            if len(usr_code.strip()) == 0:
                name = "Emtpy submission"
                shortd = "No code in the text editor"
                longd = "Please enter code before submitting solution."
                feedback = {"Name":name, "Short":shortd, "Long":longd}
                parsed_result_feedback = json.dumps([feedback])
            else:
                envFile = Assessment.objects.get(id=int(assessmentID)).assess_file.path
                testFile = self.setupEnv(usr_code, envFile, request.user)
                result_feedback = list(map(lambda x: x.decode('ASCII'), self.runCode(testFile)))
                print('RAW RESULT: {}'.format(result_feedback))
                if result_feedback[0]: #stdout
                    print("STDOUT")
                    out_string = result_feedback[0]
                    def parseLong(err):
                        span = re.search('Long.+}', err).span()
                        old = err[(span[0]+7):(span[1]-1)]
                        #print("LONG ERR0",old)
                        if "Error(" in old:
                            new = repr(old)[1:-1].replace("\'","*").replace("\"","`")
                            #print("LONG ERR1",new)
                            return(err.replace(old, "'"+new+"'"))
                        return err

                    out_string = [parseLong(err) for err in out_string.splitlines()]
                    print("OUTPUT ERROR: ", out_string)
                    errs = [{k:"{}".format(v) for k,v in (eval(err)).items()} for err in out_string]
                    print("ERRORS", errs)
                    parsed_result_feedback  = json.dumps(errs)
                elif result_feedback[1]: #stderr
                    print("STERR")
                    error_string = result_feedback[1]
                    name = "Error"
                    shortd = [x for x in error_string.split() if 'Error' in x].pop()[:-1]
                    longd =  error_string[(error_string.find(shortd)):-1] #+ error_string[(error_string.find('\n')):(error_string.find(shortd))]
                    if 'Indentation' in shortd:
                        name = 'Indentation error'
                        shortd = 'Make sure you are using tabs for indentation, and not spaces.'

                    feedback = {"Name":name, "Short":shortd, "Long":longd}
                    parsed_result_feedback = json.dumps([feedback])
                else:
                    parsed_result_feedback = "good"
                print('PARSED RESULT: {}'.format(parsed_result_feedback))
                assessment_progress = AssessmentProgress.objects.get(student=Student.objects.get(user=request.user), assessment=Assessment.objects.get(id=int(assessmentID)))
                assessment_progress.code_submission = usr_code
                assessment_progress.errors_list = parsed_result_feedback
                assessment_progress.attempted = True
                assessment_progress.number_of_attempts = assessment_progress.number_of_attempts+1
                if parsed_result_feedback == 'good':
                    assessment_progress.solved = True
                assessment_progress.save()
                ap_record = str(model_to_dict(assessment_progress))
                AssessmentSubmission.objects.create(submission_record = ap_record)
                return HttpResponse(parsed_result_feedback)
            return self.get(request, *args, **kwargs)

        elif(request.POST.get('stud_email')):
            '''
            messageContents: message
            from_address: from_address
            course_title: course_title
            module_title: module_title
            stud_first_name: stud_first_name
            stud_last_name: stud_last_name
            stud_email: stud_email
            '''
            #return HttpResponse('got it')
            #from_address = request.POST.get('from_address')
            msg = request.POST.get('messageContents')
            course_title = request.POST.get('course_title')
            module_title = request.POST.get('module_title')
            challengeID = request.POST.get('challengeID')
            stud_first_name = request.POST.get('stud_first_name')
            stud_last_name = request.POST.get('stud_last_name')
            stud_email = request.POST.get('stud_email')
            stud_code = request.POST.get('stud_code')
            error_message = request.POST.get('error_message')

            from_address = '{} {} <{}>'.format(stud_first_name, stud_last_name, stud_email)
            msg_txt = 'Course: {}\nModule: {}\nChallenge: {}\n\nCode:\n\n{}\n\nQuestion:\n\n{}\n\n{}'.format(course_title, module_title, challengeID, stud_code, msg, from_address)

            ct = '<h2 style="color: teal">Course: <em>{}</em></h2>'.format(course_title)
            mod = '<h3 style="color: LightSeaGreen">Module: <em>{}</em></h3>'.format(module_title)
            chal = '<h4 style="color: DarkSeaGreen">Challenge: <em>{}</em></h4>'.format(challengeID)
            code = '<h4>Code:</h4><pre style="border: solid gold; background-color: lightyellow; padding: 10px; margin-bottom: 20px">{}</pre>'.format(stud_code)

            error = '<h4>Errors:</h4><pre style="border: solid DarkRed; background-color: LightPink; padding: 10px; margin-bottom: 20px">{}</pre>'.format(error_message)

            #question = '<h4>Question:</h4><pre style="border: solid coral; background-color: PeachPuff; padding: 10px; margin-bottom: 10px">{}</pre>'.format(msg)
            question = '<h4>Question:</h4><pre style="border: solid SteelBlue; background-color: LightCyan; padding: 10px; margin-bottom: 10px">{}</pre>'.format(msg)

            sender = '<div>{} {} &lt;{}&gt;</div>'.format(stud_first_name, stud_last_name, stud_email)

            msg_html = '{}{}{}{}{}{}{}'.format(ct, mod, chal, code, error, question, sender)

            #print fromemail
            #ret = self.test(self.get_object())
            ret = self.send_email(self.get_object(), msg_txt, msg_html, from_address)
            return HttpResponse(ret)

    def send_email(self, user, msg_txt, msg_html, from_address):
        #site = Site.objects.get_current()
        #from_address = '%s <no-reply@%s>' % (site.name, site.domain)
        subject = "POCO user question"
        #to_addresses = ('{}'.format('manu@cs.uoregon.edu'),) #admin
        to_addresses = ['Manujinda Wathugala <manu@cs.uoregon.edu>', 'Stephen Fickas <fickas@cs.uoregon.edu>'] #admin

        #text_body = 'This is an important message1234.'

        msg = EmailMultiAlternatives(subject, msg_txt, from_address, to_addresses, reply_to=[from_address], bcc=[from_address])
        #msg = EmailMultiAlternatives('subject', 'msg_txt', 'manu@uoregon.edu', ['manu@cs.uoregon.edu'])

        msg.attach_alternative(msg_html, "text/html")

        msg.send()
        return from_address






class MenuView(generic.DetailView):
    template_name = 'main/menu.html'
    model=User

    # student_instance = user_instance.students
    # module_prog = ModuleProgress.create(student=student_instance)
    def get(self, request, *args, **kwargs):
        request.session['course_title'] = self.kwargs['course']
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        studentId = context['user'].students.id
        courseId = context['course_obj'].id
        print("REQUEST SESSION", request.session.items())
        print(studentId, courseId)
        print(CourseProgress.objects.all().values())
        print("GET context", context.items())
        if not (CourseProgress.objects.filter(student_id=studentId, course_id=courseId,approved=True)):
            request.session['approved'] = False
            return HttpResponseNotFound("<br/><br/><h1 style='text-align:center;vertical_align:middle;'>Please register for the course to access this page</h1>")

        request.session['approved'] = True
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MenuView, self).get_context_data(**kwargs)
        courses = [(slugify(c.title),c) for c in Course.objects.all()]
        course_title= self.kwargs.get('course')
        course_lookup = [c[1] for c in courses if c[0]==course_title].pop() #sloppy

        context['course_obj'] = course_lookup
        context['modules'] = Module.objects.filter(course_id=course_lookup.id)
        # setup module progress for student
        student_instance = context['object'].students
        for module_instance in context['modules']:
            module_prog,created = student_instance.moduleprogress_set.get_or_create(module=module_instance)

        return context

    def post(self, request, *args, **kwargs):
        print("UPDATE MODULE PROGRESS", request.POST.dict())
        if request.POST.get('changeButton'):
            moduleID = request.POST.get('moduleID')
            # update module progress
            module_progress = ModuleProgress.objects.get(student=Student.objects.get(user=request.user), module=Module.objects.get(id=int(moduleID)))
            module_progress.started = True
            module_progress.save()
            return HttpResponse("module progress has been saved with started=True")
        return HttpResponse("post received, no action taken by django")

class ProfileView(generic.DetailView):
    template_name = 'main/profile.html'
    model = User

    def send_email(self, user, text_body):
         text_body = 'MESSAGE:\n{} '.format(text_body)
         site = Site.objects.get_current()
         print("SITE: {}".format(site.domain))
         from_address = '%s <no-reply@%s>' % (site.name, site.domain)
         subject = "POCO user sign-up"
         to_addresses = ['manu@cs.uoregon.edu', 'fickas@cs.uoregon.edu'] #test
         #to_addresses = ('{}'.format(self.get_queryset().get(username='admin').email),) #admin
         msg = EmailMultiAlternatives(subject, text_body, from_address, to_addresses)
         msg.send()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        request.session['approved'] = False
        print("REQUEST SESSION", request.session.items())
        print("GET context", context.items())
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        # setup course progress for student
        student_instance = context['object'].students
        for course_instance in context['courses']:
            course_prog,created = student_instance.courseprogress_set.get_or_create(course=course_instance)
            print("COURSE PROGRESS for {}".format(student_instance))
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('messageContents'):
            msg = request.POST.get('messageContents')
            self.send_email(self.get_object(), msg)
            return HttpResponse("post received to send email")
        return HttpResponse("post received, no action taken by django")


class GoogleView(generic.TemplateView):
    template_name = 'main/google8a43fbed4f8a62b6.html'

class LoginView(generic.TemplateView):
    template_name = 'main/login.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        request.session['approved'] = False
        print('Get')
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        usr_token = request.POST.get('idtoken')
        user = authenticate(token=usr_token)
        print("USERID",user,user.pk)
        if user is not None:
            if user.is_active:
                login(request, user)
                print('foo')
                return HttpResponse(json.dumps({'pk':user.pk}))

                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                return HttpResponseNotFound("<br/><br/><h1 style='text-align:center;vertical_align:middle;'>Disabled account!</h1>")
        else:
            # Return an 'invalid login' error message.
            return HttpResponseNotFound("<br/><br/><h1 style='text-align:center;vertical_align:middle;'>Invalid login!</h1>")


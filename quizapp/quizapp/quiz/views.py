from django.shortcuts import render,HttpResponse,redirect
from .models import Question
from django.contrib import messages
import random


# Create your views here.
def quizhome(request):
    if request.user.is_anonymous:
        return redirect('/user/login')
    else:
        return render(request,'quiz.html')

def playquiz(request):
    # Authenticate user
    if request.user.is_anonymous:
        return redirect('/user/login')
    else:
        # Get all questions from the Question model
        questions = Question.objects.all()
        
        # Get the current question index from the session or set it to 1
        question_index = request.session.get('question_index', 1)
        
        # If all questions have been displayed, redirect or display a message
        if question_index > questions.count():
            return render(request, 'report.html')
        
        # Get the current question using the question index
        question = questions[question_index - 1]
        
        # Get options for the current question
        options = [question.option1, question.option2, question.option3, question.option4]
        
        # Shuffle options
        random.shuffle(options)
        
        if request.method == 'POST':
            # Get the selected answer from the form submission
            selected_answer = request.POST.get('answer')
            
            # Process the selected answer (e.g., check correctness, update score, etc.)
            # Add your logic here
            
            # Increment the question index for the next question
            question_index += 1
            request.session['question_index'] = question_index
        
            # Redirect to the same view to display the next question
            return redirect('playquiz')
        
        # Pass the context data to the template
        context = {'question': question, 'options': options}
        return render(request, 'play.html', context)
    
    
    # check answer
    # if answer is correct, increment score
def check_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_option = request.POST.get('selected_option')
        correct_answer = request.POST.get('correct_answer')
        
        if question_id and selected_option:
            # Check if selected option is correct
            if selected_option == correct_answer:
                # Display success message if the answer is correct
                messages.success(request, "Correct answer!")
            else:
                # Display error message if the answer is incorrect
                messages.error(request, "Incorrect answer!")
        
    return redirect('playquiz')  # Redirect back to the playquiz view


        
        
       
        
    

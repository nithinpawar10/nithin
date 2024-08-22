from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

# Landing page view
def landing_page(request):
    return render(request, 'university/landing_page.html')

# API to fetch courses
def get_courses(request, course_type):
    if course_type == 'UG':
        courses = ['B.Sc', 'B.A', 'B.Com']
    elif course_type == 'PG':
        courses = ['M.Sc', 'M.A', 'M.Com']
    return JsonResponse({'courses': courses})

# API to search for a student by ID
def search_student(request, student_id):
    try:
        student = Student.objects.get(student_id=student_id)
        return JsonResponse({'student_id': student.student_id, 'name': student.name, 'email': student.email})
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)

# API to add a new student
def add_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        email = request.POST.get('email')

        student, created = Student.objects.get_or_create(student_id=student_id, defaults={'name': name, 'email': email})
        if not created:
            student.name = name
            student.email = email
            student.save()

        return JsonResponse({'message': 'Student saved successfully'})
# Create your views here.

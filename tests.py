from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task, Category


class AuthTests(TestCase):
    def test_register_page_loads(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        response = self.client.post('/accounts/register/', {
            'username': 'newuser',
            'email': 'new@test.com',
            'password1': 'securepass123!',
            'password2': 'securepass123!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_dashboard_requires_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_dashboard_accessible_when_logged_in(self):
        User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class TaskTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        self.category = Category.objects.create(name='Work', color='#3498db', created_by=self.user)
        self.task = Task.objects.create(
            title='Test Task',
            description='Test description',
            priority='high',
            status='pending',
            owner=self.user,
            category=self.category,
        )

    def test_task_list_accessible(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        response = self.client.post('/tasks/create/', {
            'title': 'New Test Task',
            'description': 'Description here',
            'priority': 'medium',
            'status': 'pending',
            'category': self.category.pk,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Test Task').exists())

    def test_task_model_str(self):
        self.assertEqual(str(self.task), 'Test Task')

    def test_category_model_str(self):
        self.assertEqual(str(self.category), 'Work')

    def test_delete_task(self):
        response = self.client.post(f'/tasks/{self.task.pk}/delete/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
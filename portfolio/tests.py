from django.test import TestCase, Client
from django.urls import reverse

class PortfolioTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Максим Коваленко')
        self.assertContains(response, 'Python')
        self.assertContains(response, 'badge-advanced')

    def test_projects_page(self):
        response = self.client.get(reverse('portfolio:projects'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Агрегатор новин та аналітики')
        self.assertContains(response, reverse('portfolio:project_detail', args=[2]))

    def test_project_detail_page(self):
        response = self.client.get(reverse('portfolio:project_detail', args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Платформа моніторингу серверів')
        self.assertContains(response, 'В процесі')

    def test_project_detail_not_found(self):
        response = self.client.get(reverse('portfolio:project_detail', args=[999]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Проєкт не знайдено')

    def test_contacts_page(self):
        response = self.client.get(reverse('portfolio:contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Контактна інформація')
        self.assertContains(response, 'developer.portfolio@mail.net')

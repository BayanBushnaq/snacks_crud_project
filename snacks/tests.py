from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

# Create your tests here.

class SnacksTests(TestCase):
    def test_snack_ListView_status(self):
        url = reverse('snack_listview')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)

    def test_snack_ListView_template(self):
        url = reverse('snack_listview')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_ListView.html')



    # def test_Snack_DetailView_template(self):
    #     url = reverse('Snack_DetailView')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response,'Snack_DetailView.html')


    # def test_Snack_CreateView_status(self):
    #     url = reverse('Snack_CreateView')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code , 200)




    # def test_Snack_UpdateView_status(self):
    #     url = reverse('Snack_UpdateView')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code , 200)

    # def test_Snack_UpdateView_template(self):
    #     url = reverse('Snack_UpdateView')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response,'Snack_UpdateView.html')


    # def test_Snack_DeleteView_status(self):
    #     url = reverse('Snack_DeleteView')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code , 200)

    # def test_Snack_DeleteView_template(self):
    #     url = reverse('Snack_DeleteView')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response,'Snack_DeleteView.html')



    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test',
            email = 'test@test.com',
            password = 'test'
        )

        self.snack = Snack.objects.create(
            title = 'test',
            purchaser = self.user,
            description = 'Text'
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack),'test')


    def test_snack_DetailView(self):
        url = reverse('Snack_DetailView',args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'Snack_DetailView.html')

    def test_Snack_CreateView(self):
        data = {
            'title' : 'test',
            'description': 'desc',
            'purchaser' : self.user.id
        }
        url = reverse('Snack_CreateView')
        response = self.client.post(path=url,data=data,follow=True)
        self.assertEqual(len(Snack.objects.all()),2)
        self.assertTemplateUsed(response,'Snack_DetailView.html')
        self.assertRedirects(response,reverse('Snack_DetailView',args=[2]))

    

    








    


    
from django.test import TestCase
from django.urls import resolve

from helloworld.views import top, snippet_new, snippet_edit, snippet_detail

class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get('/')
        self.assertContains(response, '金川卓磨のDjangoスニペット', status_code=200)

    def test_top_page_uses_expected_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'snippets/top.html')

# Create your tests here.
#class TopPageViewTest(TestCase):
#    def test_top_returns_200(self):
#        response = self.client.get('/')
#        self.assertEqual(response.status_code, 200)

#    def test_top_returns_expected_content(self):
#        response = self.client.get('/')
#        self.assertEqual(response.content, b'Hello World')

#class CreateSnippetTest(TestCase):
#    def test_should_resolve_snippet_new(self):
#        found = resolve('/helloworld/new/')
#        self.assertEqual(snippet_new, found.func)


#class SnippetDetailTest(TestCase):
#    def test_should_resolve_snippet_detail(self):
#        found = resolve('/helloworld/1/')
#        self.assertEqual(snippet_detail, found.func)


#class EditSnippetTest(TestCase):
#    def test_should_resolve_snippet_edit(self):
#        found = resolve('/helloworld/1/edit/')
#        self.assertEqual(snippet_edit, found.func)
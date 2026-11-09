import uuid
from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from main.models import Education

class EducationAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com"
        )
        self.visitor = User.objects.create_user(
            username="visitor", password="test-password"
        )
        
        self.editor_group = Group.objects.create(name="Editor")
        self.editor_user = User.objects.create_user(
            username="editor", password="test-password"
        )
        self.editor_user.groups.add(self.editor_group)

        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            field_of_study="Sistem Informasi",
            description="Undergraduate student",
            start_year=2025,
        )

        self.list_url = reverse("api:education-list")
        self.detail_url = reverse("api:education-detail", args=[self.education.id])
        self.star_url = reverse("api:education-star", args=[self.education.id])
        
        self.payload = {
            "institution": "SMA Negeri 1",
            "field_of_study": "IPA",
            "description": "High school education",
            "start_year": 2022,
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], str(self.education.id))
        self.assertFalse(response.data[0]["is_starred"])
        self.assertEqual(self.client.get(self.detail_url).status_code, status.HTTP_200_OK)

    def test_search_and_empty_results(self):
        response = self.client.get(self.list_url, {"title": "Universitas"})
        self.assertEqual(len(response.data), 1)
        response = self.client.get(self.list_url, {"title": "not-found"})
        self.assertEqual(response.data, [])

    def test_missing_education(self):
        url = reverse("api:education-detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_visitor_cannot_write(self):
        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.assertEqual(self.client.patch(self.detail_url, {"institution": "Changed"}, format="json").status_code, 403)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(Education.objects.count(), 1)

    def test_regular_user_can_star_only(self):
        self.client.force_authenticate(user=self.visitor)
        res_star = self.client.post(self.star_url)
        self.assertEqual(res_star.status_code, status.HTTP_200_OK)
        self.assertTrue(res_star.data["is_starred"])

        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.assertEqual(self.client.patch(self.detail_url, {"institution": "Changed"}, format="json").status_code, 403)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)

    def test_editor_can_patch_but_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor_user)

        response = self.client.patch(self.detail_url, {"institution": "UI Depok"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.education.refresh_from_db()
        self.assertEqual(self.education.institution, "UI Depok")

        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertTrue(Education.objects.filter(pk=self.education.id).exists())

    def test_owner_can_create_put_patch_delete(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Education.objects.filter(pk=response.data["id"]).exists())

        res_put = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(res_put.status_code, status.HTTP_200_OK)

        res_delete = self.client.delete(self.detail_url)
        self.assertEqual(res_delete.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(res_delete.content, b"")
        self.assertFalse(Education.objects.filter(pk=self.education.id).exists())

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)
        for changes, field in [
            ({"institution": ""}, "institution"),
            ({"institution": '<img src="x" onerror="alert(1)">'}, "institution"),
        ]:
            response = self.client.post(self.list_url, {**self.payload, **changes}, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn(field, response.data)

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload, "star_count": 99, "is_starred": True,
            "starred_by_names": "forged", "starred_by": [self.visitor.id],
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
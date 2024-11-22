from rest_framework import status
from rest_framework.test import APITestCase

from app.user.models import User
from app.websocket_connection.models import WebsocketConnection


class WebsocketConnectionListAPITest(APITestCase):
    MODEL = WebsocketConnection
    PATH = "/v1/websocket_connection/"

    def setUp(self) -> None:
        # given
        self.success_user = User.objects.create_user(email="success@test.com")  # TODO: 성공 유저 사전 조건 수정
        self.failure_user = User.objects.create_user(email="failure@test.com")  # TODO: 실패 유저 사전 조건 수정
        self.MODEL.objects.bulk_create([self.MODEL() for i in range(20)])  # TODO: 테스트 데이터 추가

    def test_success_response(self):
        # when
        self.client.force_authenticate(self.success_user)  # TODO: 인증이 필요 없는 경우 제거
        response = self.client.get(self.PATH)

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 응답
        result_keys = []  # TODO: 응답 키 추가
        for data in response.data["results"]:
            self.assertListEqual(
                sorted(result_keys),
                sorted(data.keys()),
            )

    # TODO: 인증이 필요 없는 경우 제거
    def test_failure_response_authentication_failed(self):
        # when
        response = self.client.get(self.PATH)

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # TODO: 권한이 필요 없는 경우 제거
    def test_failure_response_permission_failed(self):
        # when
        self.client.force_authenticate(self.failure_user)
        response = self.client.get(self.PATH)

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class WebsocketConnectionCreateAPITest(APITestCase):
    MODEL = WebsocketConnection
    PATH = "/v1/websocket_connection/"

    def setUp(self) -> None:
        # given
        self.success_user = User.objects.create_user(email="success@test.com")  # TODO: 성공 유저 사전 조건 수정
        self.failure_user = User.objects.create_user(email="failure@test.com")  # TODO: 실패 유저 사전 조건 수정
        self.MODEL.objects.bulk_create([self.MODEL() for i in range(20)])  # TODO: 테스트 데이터 생성

    def test_success_response(self):
        # when
        self.client.force_authenticate(self.success_user)  # TODO: 인증이 필요 없는 경우 제거
        response = self.client.post(self.PATH, data={})  # TODO: 성공 요청 데이터 추가

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 응답
        self.assertDictEqual(response.data, {})  # TODO: 응답 데이터 추가

        # 디비
        self.assertTrue(self.MODEL.objects.filter(id=response.data["id"]).exists())

    def test_failure_response_invalid_failed(self):
        # when
        response = self.client.post(self.PATH, data={})  # TODO: 실패 요청 데이터 추가

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 응답
        self.assertDictEqual(response.data, {})  # TODO: 응답 데이터 추가

        # 디비
        self.assertFalse(self.MODEL.objects.filter(id=response.data["id"]).exists())

    # TODO: 인증이 필요 없는 경우 제거
    def test_failure_response_authentication_failed(self):
        # when
        response = self.client.get(self.PATH)

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # TODO: 권한이 필요 없는 경우 제거
    def test_failure_response_permission_failed(self):
        # when
        self.client.force_authenticate(self.failure_user)
        response = self.client.get(self.PATH)

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class WebsocketConnectionRetrieveAPITest(APITestCase):
    MODEL = WebsocketConnection
    PATH = "/v1/websocket_connection/{id}/"

    def setUp(self) -> None:
        # given
        self.success_user = User.objects.create_user(email="success@test.com")  # TODO: 성공 유저 사전 조건 수정
        self.failure_user = User.objects.create_user(email="failure@test.com")  # TODO: 실패 유저 사전 조건 수정
        self.instance = self.MODEL.objects.create()  # TODO: 테스트 데이터 생성

    def test_success_response(self):
        # when
        self.client.force_authenticate(self.success_user)  # TODO: 인증이 필요 없는 경우 제거
        response = self.client.get(self.PATH.format(id=self.instance.id))

        # then
        # 상대값
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 응답
        self.assertDictEqual(response.data, {})  # TODO: 응답 데이터 추가

    # TODO: 인증이 필요 없는 경우 제거
    def test_failure_response_authentication_failed(self):
        # when
        response = self.client.get(self.PATH.format(id=self.instance.id))

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # TODO: 권한이 필요 없는 경우 제거
    def test_failure_response_permission_failed(self):
        # when
        self.client.force_authenticate(self.failure_user)
        response = self.client.get(self.PATH.format(id=self.instance.id))

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class WebsocketConnectionUpdateAPITest(APITestCase):
    MODEL = WebsocketConnection
    PATH = "/v1/websocket_connection/{id}/"

    def setUp(self) -> None:
        # given
        self.success_user = User.objects.create_user(email="success@test.com")  # TODO: 성공 유저 사전 조건 수정
        self.failure_user = User.objects.create_user(email="failure@test.com")  # TODO: 실패 유저 사전 조건 수정
        self.instance = self.MODEL.objects.create()  # TODO: 테스트 데이터 생성

    def test_success_response(self):
        # when
        self.client.force_authenticate(self.success_user)  # TODO: 인증이 필요 없는 경우 제거
        response = self.client.put(self.PATH.format(id=self.instance.id), data={})  # TODO: 성공 요청 데이터 추가

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 응답
        self.assertDictEqual(response.data, {})  # TODO: 응답 데이터 추가

        # 디비
        self.assertFalse(self.MODEL.objects.filter(id=self.instance.id).exists())

    def test_failure_response(self):
        # when
        self.client.force_authenticate(self.success_user)  # TODO: 인증이 필요 없는 경우 제거
        response = self.client.put(self.PATH.format(id=self.instance.id), data={})  # TODO: 실패 요청 데이터 추가

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 응답
        self.assertDictEqual(response.data, {})  # TODO: 응답 데이터 추가

    # TODO: 인증이 필요 없는 경우 제거
    def test_failure_response_authentication_failed(self):
        # when
        response = self.client.get(self.PATH.format(id=self.instance.id))

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # TODO: 권한이 필요 없는 경우 제거
    def test_failure_response_permission_failed(self):
        # when
        self.client.force_authenticate(self.failure_user)
        response = self.client.get(self.PATH.format(id=self.instance.id))

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class WebsocketConnectionDestroyAPITest(APITestCase):
    MODEL = WebsocketConnection
    PATH = "/v1/websocket_connection/{id}/"

    def setUp(self) -> None:
        # given
        self.success_user = User.objects.create_user(email="success@test.com")  # TODO: 성공 유저 사전 조건 수정
        self.failure_user = User.objects.create_user(email="failure@test.com")  # TODO: 실패 유저 사전 조건 수정
        self.instance = self.MODEL.objects.create()  # TODO: 성공 테스트 데이터 생성

    def test_success_response(self):
        # when
        self.client.force_authenticate(self.success_user)  # TODO: 인증이 필요 없는 경우 제거
        response = self.client.delete(self.PATH.format(id=self.instance.id))

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # 응답
        self.assertIsNone(response.data)

        # 디비
        self.assertFalse(self.MODEL.objects.filter(id=self.instance.id).exists())

    # TODO: 인증이 필요 없는 경우 제거
    def test_failure_response_authentication_failed(self):
        # when
        response = self.client.get(self.PATH.format(id=self.instance.id))

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # TODO: 권한이 필요 없는 경우 제거
    def test_failure_response_permission_failed(self):
        # when
        self.client.force_authenticate(self.failure_user)
        response = self.client.get(self.PATH.format(id=self.instance.id))

        # then
        # 상태값
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

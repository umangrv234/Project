import requests
import logging

from APIConstants import APIConstants
from JSONBody import JSONBody

logger = logging.getLogger(__name__)


class CreateMultiplePets:

    def createMultiplePet(self, body=None):
        url = APIConstants.CREATE_PET_URI
        body = JSONBody.createPet
        request = requests.post(url, json=body)
        requestResponse = request.json()
        logger.info("The request response is %s" % requestResponse)

        return request.status_code, requestResponse

    def updatePetStatus(self, status):

        body = JSONBody.updatePet
        body['status'] = status

        url = APIConstants.CREATE_PET_URI
        request = requests.put(url=url, json=body)
        requestResponse = request.json()
        logger.info("The request response is %s" % requestResponse)

        return request.status_code, requestResponse

    def getPetByStatus(self, status):
        JSONBody.createPet['status'] = status
        body = JSONBody.createPet
        _, requestResponse = self.createMultiplePet(body=body)
        id1 = requestResponse['id']
        requestUrl = "https://petstore.swagger.io/v2/pet/findByStatus?status=%s" % status
        request = requests.get(url=requestUrl)
        requestResponse = request.json()
        logger.info("The request response is %s" % requestResponse)
        for i in range(1, len(requestResponse)):
            id = requestResponse[i]['id']

            if id == id1:
                print(id)
                verifyUpdatedStatus = requestResponse[i]['status']
                break
            else:
                verifyUpdatedStatus = None

        return request.status_code, requestResponse, verifyUpdatedStatus

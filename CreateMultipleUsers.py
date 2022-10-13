import logging
import string
import time

import requests
import random

logger = logging.getLogger(__name__)


class MultipleUsers:

    def __init__(self):

        randomGeneration = ''.join(random.choice(string.ascii_lowercase) for x in range(8))
        self.id = random.randint(1, 1000)
        self.userName = 'username%s' % randomGeneration
        self.firstName = 'firstName%s' % randomGeneration
        self.lastName = 'lastName%s' % randomGeneration
        self.email = 'emailid@%s' % randomGeneration
        self.password = 'password%s' % randomGeneration
        self.phone = 'phone%s' % randomGeneration
        self.userStatus = 0
        self.body = {"id": self.id,
                     "username": self.userName,
                     "firstName": self.firstName,
                     "lastName": self.lastName,
                     "email": self.email,
                     "password": self.password,
                     "phone": self.phone,
                     "userStatus": self.userStatus
                     }

    def createMultipleUsers(self, noOfUsers, body={}, inputParameter=False):
        jsonArray = []
        for i in range(noOfUsers):
            if inputParameter:
                self.body = body
            else:
                self.__init__()
            jsonArray.append(self.body)
        endpoint = "/v2/user/createWithArray"
        url = "https://petstore.swagger.io" + endpoint
        request = requests.post(url, json=jsonArray)
        requestResponse = request.json()
        logger.info("The request response is %s" % requestResponse)
        return request.status_code,

    def updateUserName(self, getuserName, updateUserName):
        getUserNameURLEndPoint = "/v2/user/%s" % getuserName
        url = "https://petstore.swagger.io" + getUserNameURLEndPoint
        request = requests.get(url)
        requestResponse = request.json()
        valueToBeUpdated = updateUserName
        requestResponse['username'] = valueToBeUpdated
        requestResponse = requests.put(url, json=requestResponse)
        logger.info("The request response is %s" % requestResponse)

        return request.status_code, requestResponse

    def getUsername(self, updatedUserName):
        getUserNameURLEndPoint = "/v2/user/%s" % updatedUserName
        url = "https://petstore.swagger.io" + getUserNameURLEndPoint
        request = requests.get(url)
        requestResponse = request.json()
        logger.info("The request response is %s" % requestResponse)

        return request.status_code, requestResponse

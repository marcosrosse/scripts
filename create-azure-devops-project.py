import requests
import json


authorization = "YOUR AZURE DEVOPS KEY"
base__url = "BASE URL OF AZURE DEVOPS"
dev__netcore__pipeline = (
  'IN BASE64'
)
uat__netcore__pipeline = (
  'IN BASE64'
)




def createProject():
  global project__name
  project__name = input ("Enter here the project name: ")
  description = input ("Enter here a brief description of your project: ")
  url = 'https://{}_apis/projects?api-version=5.1'.format(base__url)

  payload = json.dumps({
    "name": f"{project__name}",
    "description": f"{description}",
    "capabilities": {
      "versioncontrol": {
        "sourceControlType": "Git"
      },
      "processTemplate": {
        "templateTypeId": "b8a3a935-7e91-48b8-a94c-606d37c3e9f2"
      }
    }
  })
  headers = {
    'Authorization': f'{authorization}',
    'Content-Type': 'application/json'
  }
  requests.packages.urllib3.disable_warnings()
  response = requests.request("POST", url, headers=headers, data=payload, verify=False)
  print (response.status_code)

def createEndpoint():
    clientResponse = ''
    while clientResponse != 0:
      clientResponse = input("What kind of service connection do you want (inform the number)? 1) Openshift, 2) Checkmarx, 3) SonarQube, 4) Artifacts, 5) Nexus -- 0) QUIT): ")
      endpointsConnections = {
        '1': {
          'endpointName': 'Openshift',
          'endpointType': 'Openshift',
          'endpointUrl': '',
          'endpointUsername': '',
          'endpointPassword': '',
        },
        '2': {
          'endpointName': 'Checkmarx',
          'endpointType': 'Checkmarx-Endpoint',
          'endpointUrl': '',
          'endpointUsername': '',
          'endpointPassword': '',
        },
        '3': {
          'endpointName': 'SonarQube',
          'endpointType': 'SonarQube',
          'endpointUrl': '',
          'endpointUsername': '',
          'endpointPassword': '',
        },
        '4': {
          'endpointName': 'Artifacts',
          'endpointType': 'externalnugetfeed',
          'endpointUrl': '',
          'endpointUsername': '',
          'endpointPassword': '',
        },
        '5': {
          'endpointName': 'Nexus',
          'endpointType': 'externalnugetfeed',
          'endpointUrl': '',
          'endpointUsername': '',
          'endpointPassword': '',
        }
      }
      if clientResponse in endpointsConnections:
          connection = endpointsConnections[clientResponse]
          url = 'https://{}{}/_apis/serviceendpoint/endpoints?api-version=5.1-preview.2'.format(base__url, project__name)

          payload = json.dumps({
            "data": {},
            "name": connection['endpointName'],
            "type": connection['endpointType'],
            "url": connection['endpointUrl'],
            "authorization": {
              "parameters": {
                "username": connection['endpointUsername'],
                "password": connection['endpointPassword']
              },
              "scheme": "UsernamePassword"
            },
            "isShared": True,
            "isReady": True
          })
          headers = {
            'Authorization': f'{authorization}',
            'Content-Type': 'application/json'
          }
          requests.packages.urllib3.disable_warnings()
          response = requests.request("POST", url, headers=headers, data=payload, verify=False)
          print (response.status_code)
      elif clientResponse != '0' and endpointsConnections:
        print ('Non-existent service connection. If possible, register manualy')
      else:
        return None

def addPipelineFiles():
  url = 'https://{}{}/_apis/git/repositories/{}/pushes?api-version=5.1'.format(base__url, project__name, project__name)

  payload = json.dumps({
    "refUpdates": [
      {
        "name": "refs/heads/develop",
        "oldObjectId": "00000000000000000000000000000"
      }
    ],
    "commits": [
      {
        "comment": "Add pipelines",
        "changes": [
          {
            "changeType": "add",
            "item": {
              "path": "/dev-azure-pipelines.yml"
            },
            "newContent": {
              "content": f'{dev__netcore__pipeline}',
              "contentType": "base64encoded"
            }
          },
          {
            "changeType": "add",
            "item": {
              "path": "/uat-azure-pipelines.yml"
            },
            "newContent": {
              "content": f'{uat__netcore__pipeline}',
              "contentType": "base64encoded"
            }
          }
        ]
      }
    ]
  })
  headers = {
    'Authorization': f'{authorization}',
    'Content-Type': 'application/json'
  }
  requests.packages.urllib3.disable_warnings()
  response = requests.request("POST", url, headers=headers, data=payload, verify=False)
  print (response.status_code)


createProject()
createEndpoint()
addPipelineFiles()
# def main ():
#     createProject()
#     createEndpoint()
#     addPipelineFiles()

# if __name__ == '__main__':
#   main()

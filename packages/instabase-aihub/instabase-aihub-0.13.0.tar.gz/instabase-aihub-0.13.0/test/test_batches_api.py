import json
import unittest
from unittest.mock import patch

import urllib3
from aihub import AIHub


class TestBatchesApi(unittest.TestCase):
  """BatchesApi unit test stubs"""

  def setUp(self) -> None:
    self.client = AIHub(api_key='TEST_API_KEY')

  def tearDown(self) -> None:
    pass

  @patch.object(urllib3.PoolManager, 'request')
  def test_add_file_to_batch(self, mock_request) -> None:
    """Test case for add_file_to_batch

        Upload a file to the batch.
        """
    batch_id = 10
    filename = 'file.txt'
    file_content = b'File content'

    # Mock the HTTP PUT request response
    mock_response = urllib3.HTTPResponse(body=b' ', status=204)
    mock_request.return_value = mock_response

    # Act
    self.client.batches.add_file(batch_id, filename, file_content)
    mock_request.assert_called_once()

  @patch.object(urllib3.PoolManager, 'request')
  def test_list_files(self, mock_request) -> None:
    """Test case for list_files

        List files in a batch.
        """
    batch_id = 10
    expected_response = {
        "nodes": [{
            "name": "file.txt",
            "size": 100,
            "type": "file"
        }]
    }

    # Mock the HTTP GET request response
    mock_response = urllib3.HTTPResponse(
        body=bytes(json.dumps(expected_response), 'utf-8'), status=200)
    mock_request.return_value = mock_response

    # Act
    response = self.client.batches.list_files(batch_id)
    mock_request.assert_called_once()

    # Assert
    self.assertEqual(response.nodes[0].name,
                     expected_response['nodes'][0]['name'])
    self.assertEqual(1, len(response.nodes))

  @patch.object(urllib3.PoolManager, 'request')
  def test_create_batch(self, mock_request) -> None:
    """Test case for create_batch

        Create a new batch.
        """
    expected_response = {"id": 10}

    # Mock the HTTP POST request response
    mock_response = urllib3.HTTPResponse(
        body=bytes(json.dumps(expected_response), 'utf-8'), status=200)
    mock_request.return_value = mock_response

    # Act
    response = self.client.batches.create("test batch")
    mock_request.assert_called_once()

    # Assert
    self.assertEqual(response.id, expected_response['id'])

  @patch.object(urllib3.PoolManager, 'request')
  def test_delete_batch(self, mock_request) -> None:
    """Test case for delete_batch

        Delete a batch and all of its files.
        """
    batch_id = 10
    expected_response = {"job_id": "AA"}

    # Mock the HTTP DELETE request response
    mock_response = urllib3.HTTPResponse(
        body=bytes(json.dumps(expected_response), 'utf-8'), status=202)
    mock_request.return_value = mock_response

    # Act
    response = self.client.batches.delete(batch_id)
    mock_request.assert_called_once()

    # Assert
    self.assertEqual(response.job_id, expected_response['job_id'])

  @patch.object(urllib3.PoolManager, 'request')
  def test_delete_file_from_batch(self, mock_request) -> None:
    """Test case for delete_file_from_batch

        Delete a file from a batch.
        """
    batch_id = 10
    filename = 'file.txt'

    # Mock the HTTP DELETE request response
    mock_response = urllib3.HTTPResponse(body=b' ', status=202)
    mock_request.return_value = mock_response

    # Act
    self.client.batches.delete_file(batch_id, filename)

    # Inspect the call arguments
    actual_method, actual_url = mock_request.call_args[0][
        0], mock_request.call_args[0][1]

    # Assert method and URL
    self.assertEqual(actual_method, 'DELETE')
    self.assertEqual(
        actual_url,
        f'{self.client.client.configuration.host}/v2/batches/{batch_id}/files/{filename}'
    )

  @patch.object(urllib3.PoolManager, 'request')
  def test_get_batch(self, mock_request) -> None:
    """Test case for get_batch

        Retrieve information about a batch.
        """
    batch_id = 10
    expected_response = {"id": 10, "name": "test batch"}

    # Mock the HTTP GET request response
    mock_response = urllib3.HTTPResponse(
        body=bytes(json.dumps(expected_response), 'utf-8'), status=200)
    mock_request.return_value = mock_response

    # Act
    response = self.client.batches.get(batch_id)
    mock_request.assert_called_once()

    # Assert
    self.assertEqual(response.id, expected_response['id'])
    self.assertEqual(response.name, expected_response['name'])

  @patch.object(urllib3.PoolManager, 'request')
  def test_list_batches(self, mock_request) -> None:
    """Test case for list_batches

        Return a list of batches.
        """
    expected_response = {"batches": [{"id": 10, "name": "test batch"}]}

    # Mock the HTTP GET request response
    mock_response = urllib3.HTTPResponse(
        body=bytes(json.dumps(expected_response), 'utf-8'), status=200)
    mock_request.return_value = mock_response

    # Act
    response = self.client.batches.list()
    mock_request.assert_called_once()

    # Assert
    self.assertEqual(len(response.batches), 1)
    self.assertEqual(response.batches[0].id,
                     expected_response['batches'][0]['id'])
    self.assertEqual(response.batches[0].name,
                     expected_response['batches'][0]['name'])

  @patch.object(urllib3.PoolManager, 'request')
  def test_poll_batches_job(self, mock_request) -> None:
    """Test case for poll_batches_job

        Poll the status of asynchronous jobs for batches.
        """
    job_id = "abc123"
    expected_response = {
        "state": "COMPLETE",
        "message": "Job completed successfully"
    }

    # Mock the HTTP GET request response
    mock_response = urllib3.HTTPResponse(
        body=bytes(json.dumps(expected_response), 'utf-8'), status=200)
    mock_request.return_value = mock_response

    # Act
    response = self.client.batches.poll_job(job_id)
    mock_request.assert_called_once()

    # Assert
    self.assertEqual(response.state, expected_response['state'])
    self.assertEqual(response.message, expected_response['message'])

  @patch.object(urllib3.PoolManager, 'request')
  def test_create_multipart_upload_session(self, mock_request) -> None:
    """Test case for create_multipart_upload_session

        Start a multipart upload session for large files.
        """
    batch_id = 123
    filename = "large_file.pdf"
    file_size = 15728640
    expected_response = {"part_size": 5242880, "session_id": "abc123"}
    expected_location = f"{self.client.client.configuration.host}/v2/batches/multipart-upload/sessions/abc123"

    # Mock the HTTP POST request response
    mock_response = urllib3.HTTPResponse(
        body=bytes(json.dumps(expected_response), 'utf-8'), status=201)
    # Add Location header to mock response
    mock_response._original_response = type('MockOriginalResponse', (), {})()
    mock_response._original_response.msg = type('MockMessage', (), {})()
    mock_response._original_response.msg.get = lambda x, default=None: expected_location if x.lower(
    ) == 'location' else default
    mock_request.return_value = mock_response

    # Act
    response = self.client.batches.create_multipart_upload_session(
        batch_id, filename, file_size)
    mock_request.assert_called_once()

    # Inspect the call arguments
    actual_method, actual_url = mock_request.call_args[0][
        0], mock_request.call_args[0][1]
    actual_body = json.loads(mock_request.call_args[1]['body'])

    # Assert method and URL
    self.assertEqual(actual_method, 'POST')
    self.assertEqual(
        actual_url,
        f'{self.client.client.configuration.host}/v2/batches/multipart-upload')

    # Assert request body
    self.assertEqual(actual_body['batch_id'], batch_id)
    self.assertEqual(actual_body['filename'], filename)
    self.assertEqual(actual_body['file_size'], file_size)

    # Assert response
    self.assertEqual(response.part_size, expected_response['part_size'])
    self.assertEqual(response.session_id, expected_response['session_id'])

  @patch.object(urllib3.PoolManager, 'request')
  def test_upload_multipart_part(self, mock_request) -> None:
    """Test case for upload_multipart_part

        Upload a part to an active multipart upload session.
        """
    session_id = "abc123"
    part_num = 1
    part_data = b"This is part 1 of the file content"
    expected_response = {"part_id": "12345", "part_num": 1}

    # Mock the HTTP PUT request response
    mock_response = urllib3.HTTPResponse(
        body=bytes(json.dumps(expected_response), 'utf-8'), status=201)
    mock_request.return_value = mock_response

    # Act
    response = self.client.batches.upload_multipart_part(
        session_id, part_num, part_data)
    mock_request.assert_called_once()

    # Inspect the call arguments
    actual_method, actual_url = mock_request.call_args[0][
        0], mock_request.call_args[0][1]
    actual_body = mock_request.call_args[1]['body']

    # Assert method and URL
    self.assertEqual(actual_method, 'PUT')
    self.assertEqual(
        actual_url,
        f'{self.client.client.configuration.host}/v2/batches/multipart-upload/sessions/{session_id}/parts/{part_num}'
    )

    # Assert request body
    self.assertEqual(actual_body, part_data)

    # Assert response
    self.assertEqual(response.part_id, expected_response['part_id'])
    self.assertEqual(response.part_num, expected_response['part_num'])

  @patch.object(urllib3.PoolManager, 'request')
  def test_commit_multipart_upload_session(self, mock_request) -> None:
    """Test case for commit_multipart_upload_session

        Commit or abort a multipart upload session.
        """
    session_id = "abc123"
    action = "commit"
    parts = [{
        "part_num": 1,
        "part_id": "12345"
    }, {
        "part_num": 2,
        "part_id": "12346"
    }]

    # Mock the HTTP POST request response (201 Created)
    mock_response = urllib3.HTTPResponse(body=b' ', status=201)
    mock_request.return_value = mock_response

    # Act
    self.client.batches.commit_multipart_upload_session(
        session_id, action, parts)
    mock_request.assert_called_once()

    # Inspect the call arguments
    actual_method, actual_url = mock_request.call_args[0][
        0], mock_request.call_args[0][1]
    actual_body = json.loads(mock_request.call_args[1]['body'])

    # Assert method and URL
    self.assertEqual(actual_method, 'POST')
    self.assertEqual(
        actual_url,
        f'{self.client.client.configuration.host}/v2/batches/multipart-upload/sessions/{session_id}'
    )

    # Assert request body
    self.assertEqual(actual_body['action'], action)
    self.assertEqual(len(actual_body['parts']), 2)
    self.assertEqual(actual_body['parts'][0]['part_num'], 1)
    self.assertEqual(actual_body['parts'][0]['part_id'], "12345")
    self.assertEqual(actual_body['parts'][1]['part_num'], 2)
    self.assertEqual(actual_body['parts'][1]['part_id'], "12346")

  @patch.object(urllib3.PoolManager, 'request')
  def test_commit_multipart_upload_session_abort(self, mock_request) -> None:
    """Test case for commit_multipart_upload_session with abort action

        Abort a multipart upload session.
        """
    session_id = "abc123"
    action = "abort"

    # Mock the HTTP POST request response (201 Created)
    mock_response = urllib3.HTTPResponse(body=b' ', status=201)
    mock_request.return_value = mock_response

    # Act
    self.client.batches.commit_multipart_upload_session(session_id, action)
    mock_request.assert_called_once()

    # Inspect the call arguments
    actual_method, actual_url = mock_request.call_args[0][
        0], mock_request.call_args[0][1]
    actual_body = json.loads(mock_request.call_args[1]['body'])

    # Assert method and URL
    self.assertEqual(actual_method, 'POST')
    self.assertEqual(
        actual_url,
        f'{self.client.client.configuration.host}/v2/batches/multipart-upload/sessions/{session_id}'
    )

    # Assert request body
    self.assertEqual(actual_body['action'], action)
    self.assertNotIn('parts',
                     actual_body)  # parts should not be included for abort


if __name__ == '__main__':
  unittest.main()

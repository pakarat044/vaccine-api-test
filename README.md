# vaccine-api-test of Flamxby group

## Endpoint
- testing when `GET` the specific reservations detail from reservation id.

## Testcast
| List of test cases | Name                                                 | Description                                                                                                  | Result |
|--------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------|
| 1                  | test_reservation_id_succeed                          | This function test that the website can GET reservation id to succeed.                                       | pass   |
| 2                  | test_reservation_id_input_negative_number            | This function test that it should not find information when the input a reservation id is a negative number. | pass   |
| 3                  | test_reservation_id_input_not_exist                  | This function test that it should not find information when the input reservation id does not exist.         | pass   |
| 4                  | test_reservation_id_are_get_correct_response_body    | This function test that the input reservation id and get information on that reservation id.                 | pass   |
| 5                  | test_reservation_id_are_get_correct_response_headers | This function test that the input reservation id and get correct response headers.                           | pass   |

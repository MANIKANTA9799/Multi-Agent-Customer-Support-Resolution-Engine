from uuid import UUID


def test_create_ticket_success(client):
 response = client.post(
"/api/v1/tickets",
 json={
 "subject": "Test Subject",
 "message": "Test Message"
}
 )

 assert response.status_code == 202

 data = response.json()

 assert data["status"] == "queued"

 ticket_id = data["id"]

 UUID(ticket_id)
start-local-backend:
	docker compose -f backend/docker-compose.yaml up


stop-local-backend:
	docker compose -f backend/docker-compose.yaml down 

create-crypto-bucket:
	aws --endpoint-url http://localhost:9000 s3api  create-bucket --bucket crypto
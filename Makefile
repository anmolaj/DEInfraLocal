run-minio:
	echo "Create Data folder if not exists for the container"
	mkdir -p data
	echo "Run Minio server in background"
	docker stop minio  
	docker rm minio || True

	docker run -d -p 9000:9000 -p 9001:9001 \
	 --name minio quay.io/minio/minio \
	 server /data \
	 --console-address ":9001"


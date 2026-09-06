import docker

# Create a Docker client
client = docker.from_env()

# Build the Docker image
print("Building Docker image: flask-apparmor...")
client.images.build(path=".", tag="flask-apparmor")

# Run the container with the AppArmor profile
print("Running container with AppArmor security-opt...")
container = client.containers.run(
    "flask-apparmor",
    ports={'5000/tcp': 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

print(f"Container started: {container.short_id}")

# Verify AppArmor profile applied
container_info = client.api.inspect_container(container.id)
apparmor_profile = container_info['HostConfig']['SecurityOpt']

print(f"AppArmor profile applied: {apparmor_profile}")

# Stop and clean up container
print("Stopping and cleaning up container...")
container.stop()
container.remove()
print("Finished successfully.")

clear
username="email"

# This commando get's a password from the apple keychain.
password=$(security find-internet-password -a "PAT" -w)

yourIpAddress=$(curl -s https://ipinfo.io/json | jq -r '.ip')

payload=$(echo "
    {
      \"templateParameters\": {
        \"yourIpAddress\": \"${yourIpAddress}\"
      }
    }" | jq -c)

echo "===========Whitelisting IP ${yourIpAddress}==========="

response=$(curl \
    --silent \
    --request POST \
    --data "${payload}" \
    --url "<ENDPOINT>" \
    --header "Content-Type: application/json" \
    --user "${username}":"${password}")
echo "===========Pipeline started!==========="

href=$(echo $response | sed 's/\\kube/kube/g' | jq -r '._links.self.href')

response= $(curl $href --user "${username}":"${password}")

responseState=$(echo $response | sed 's/\\kube/kube/g' | jq -r '.state')

while [ "completed" != "$responseState" ] ; do
  echo "===========Waiting for pipeline to finish!...==========="
  sleep 15 
  response=$(curl $href --user "${username}":"${password}")
  responseState=$(echo $response | sed 's/\\kube/kube/g' | jq -r '.state')
done

echo "===========IP Added!==========="
clear 
echo "===========Logging into AZ==========="
az login

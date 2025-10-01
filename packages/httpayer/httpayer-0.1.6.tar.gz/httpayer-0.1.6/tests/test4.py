from httpayer import HTTPayerClient
import json

def main(urls):

    """Test the HTTPayerClient with multiple URLs.
    This function sends POST requests to the provided URLs and prints the response headers,
    status codes, and response bodies. It is designed to test the functionality of the HTTPayerClient
    with multiple endpoints that are expected to return 402 Payment Required responses.

    Args:
        urls (list): A list of URLs to test with the HTTPayerClient.
    
    """

    responses = []

    for url in urls:
        print(f'processing {url}...')

        client = HTTPayerClient()
        response = client.request("POST", url)

        print(f'response headers: {response.headers}')  # contains the x-payment-response header
        print(f'response status code: {response.status_code}')  # should be 200 OK
        print(f'response text: {response.text}')  # contains the actual resource
        try:
            print(f'response json: {response.json()}')  # if the response is JSON, print it
        except ValueError:
            print("Response content is not valid JSON")

        responses.append(response)

    return responses

if __name__ == "__main__":
    print(f'starting test4...')
    urls = ["https://x402-ai-starter-rho-sepia.vercel.app/api/add"]
    main(urls)

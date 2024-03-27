#!/bin/bash
# Get the response body for a given URL for 200 status code responses.

URL=$1
curl -sL -o /dev/null -w "%{http_code}" "$URL" | grep -q "^200$" && curl -sL "$URL"
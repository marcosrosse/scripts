#!/bin/bash
# Simple script to delete the latest images in Harbor before uploading a new image.
# Run this in your CI/CD pipeline

case "${{parameters.environment}}" in
    "dev")
        STATUS_CODE=$(curl -u "$HARBOR_USER:$HARBOR_PASS" --location --request GET "https://$HOST/api/v2.0/projects/$PROJECT/repositories/$REPO_NAME/artifacts/${{parameters.tag}}" -k --write-out "%{http_code}\n" --silent --output /dev/null)

        case "$STATUS_CODE" in
            404)
                echo "There's no such tag or image in this repository. Status code: $STATUS_CODE"
                exit 0
                ;;

            200)
                STATUS_CODE=$(curl -u "$HARBOR_USER:$HARBOR_PASS" --location --request DELETE "https://$HARBOR_HOST/api/v2.0/projects/$PROJECT/repositories/$REPO_NAME/artifacts/${{parameters.tag}}" -k --write-out "%{http_code}\n" --silent --output /dev/null)

                if [ "$STATUS_CODE" = 200 ]; then
                    echo "Image deleted in Harbor. Status code: $STATUS_CODE"
                    exit 0
                else
                    echo "Error when trying to delete the image. Status Code: $STATUS_CODE"
                    exit 1
                fi
                ;;

            *)
                ;;
        esac
        ;;

    "tst" | "uat" | "prd")
        echo "${{parameters.environment^^}} environment. Actually, there is no need to delete an image."
        ;;

    *)
        ;;
esac

import boto3


def publish_sns(domain_dict, days_left):
    plain_message = ""
    customer = "[smileshark]"
    sns_client = boto3.client("sns")
    for k, v in domain_dict.items():
        plain_message += k + " 만기 일자가 " + str(v) + "일 남았습니다." + "\n"

    response = sns_client.publish(
        TargetArn="Input SNS ARN",
        Message=plain_message,
        Subject=customer + "domain 만기일 안내",
        #   MessageStructure = 'json'
    )
    return response

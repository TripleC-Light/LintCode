"""
Every email consists of a local name and a domain name, separated by
the @ sign.

For example, in alice@lintcode.com, alice is the local name,
and lintcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of
an email address, mail sent there will be forwarded to the same address
without dots in the local name. For example,
"alice.z@lintcode.com" and "alicez@lintcode.com" forward to the same
email address. (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first
plus sign will be ignored. This allows certain emails to be filtered,
for example m.y+name@email.com will be forwarded to my@email.com.
(Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.
How many different addresses actually receive mails?

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.

EX 1:

input: ["test.email+alex@lintcode.com","test.e.mail+bob.cathy@lintcode.com","testemail+david@lin.tcode.com"]
output: 2
explan: acturelly receive "testemail@lintcode.com" and "testemail@lin.tcode.com" 。
"""

class Solution:
    """
    @param emails: 
    @return: The number of the different email addresses
    """
    def numUniqueEmails(self, emails):
        # write your code here
        emailList = []
        for email in emails:
            local = email.split('@')
            domain = local[1]
            local = local[0].replace('.', '')
            local = local.split('+')
            local = local[0]
            realEmail = local + '@' + domain

            if realEmail not in emailList:
                emailList.append(realEmail)
                
            print(email)
            print(realEmail)
            print('----')
            
        return len(emailList)

if __name__ == '__main__':

    A = Solution()
    print(A.numUniqueEmails(["test.email+alex@lintcode.com","test.e.mail+bob.cathy@lintcode.com","testemail+david@lin.tcode.com"]))
    

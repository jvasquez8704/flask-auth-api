hey -n 1000 -c 200 -m POST 'https://api-dev.katchplus.com/users/signin' \
-T 'Content-Type: application/json' \
-d '{"email":"manolitodiceadios37@gmail.com","password":"Pass!23457!"}'



hey -n 1000 -c 200 -m POST 'https://api-dev.katchplus.com/users/signup' \
-T 'Content-Type: application/json' \
-d '{"email":"testperformance01@gmail.com","password":"Pass!23457!","forename":"Test Performance","surname":"Performance","phoneNumber":"33662255","country":"US","language":"eng","age": true,"instagram":"@test01","tcVersion":"1.0","ppVersion":"1.0"}'
myfile = ['hello.txt', 'hello.1.txt', 'hello.2.txt', 'hello.3.txt']
cmd = [ 'exit',
       'sho ip inter brief',
       'show ver',
       'show flash:' ]
x = my_netmiko('172.16.77.199', 'liam', 'Fender7797', myfile, cmd)
x.main()



myfile = ['hello.txt', 'hello.1.txt', 'hello.2.txt', 'hello.3.txt']
cmd = [ 'exit',
       'sho ip inter brief',
       'show ver',
       'show flash:' ]
x = my_netmiko('172.16.77.199', 'liam', 'Fender7797', cmd)
x.main()
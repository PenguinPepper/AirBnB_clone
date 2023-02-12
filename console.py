#!/usr/bin/python3
import cmd
'''Commandline'''


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_EOF(self, line):
        '''EOF command to exit the program'''

        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''

        return True

    def emptyline(self):
        '''Override emptyline'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()


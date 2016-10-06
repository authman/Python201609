"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from flask import Flask, render_template, request, redirect, session
import string
import random

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

    def index(self):
        if not session.has_key('count'):
            session['count'] = 1
        else:
            session['count'] += 1
        word = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(1,15))
        return self.load_view('index.html', count=session['count'], word=word)

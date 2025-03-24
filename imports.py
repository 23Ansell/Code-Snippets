from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import uuid
from datetime import datetime
import os
from dotenv import load_dotenv
import requests
from datetime import datetime, date, timedelta
from flask import request
module.exports = {
  apps : [{
    name: 'my-django-app-2',
    script: 'manage.py',
    args: 'runserver 0.0.0.0:8100',
    interpreter: 'python3',
    env: {
      PYTHONUNBUFFERED: '1',
    }
  }]
};

define({ "api": [  {    "type": "post",    "url": "/api-token-auth/",    "title": "Récupérer le token d'authentification",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "<p>String</p> ",            "optional": false,            "field": "username",            "description": "<p>Nom d'utilisateur</p> "          },          {            "group": "Parameter",            "type": "<p>String</p> ",            "optional": false,            "field": "password",            "description": "<p>Mot de passe</p> "          }        ]      }    },    "version": "0.1.0",    "name": "api_token_auth",    "group": "Authentification",    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "<p>String</p> ",            "optional": false,            "field": "token",            "description": "<p>Token d'authentification</p> "          }        ]      },      "examples": [        {          "title": "Success-Response:",          "content": "HTTP 200 OK\n{\n    \"token\": \"a_token\"\n}",          "type": "json"        }      ]    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "BADREQUEST",            "description": "<p>La paire nom d'utilisateur / mot de passe n'est pas valide</p> "          }        ]      },      "examples": [        {          "title": "Bad-request:",          "content": "HTTP 400 BAD REQUEST\n{\n    \"non_field_errors\": [\n        \"Unable to login with provided credentials.\"\n        ]\n}",          "type": "json"        }      ]    },    "filename": "./backoffice/restapi/views.py",    "groupTitle": "Authentification"  },  {    "type": "get",    "url": "/classes/",    "title": "Récupérer les classes de l'utilisateur",    "version": "0.1.0",    "name": "GetClasses",    "group": "Classes",    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "<p>Object[]</p> ",            "optional": false,            "field": "classes",            "description": "<p>Liste des classes</p> "          },          {            "group": "Success 200",            "type": "<p>Number</p> ",            "optional": false,            "field": "classes.id",            "description": "<p>ID de la classe</p> "          },          {            "group": "Success 200",            "type": "<p>String</p> ",            "optional": false,            "field": "classes.name",            "description": "<p>Nom de la classe</p> "          },          {            "group": "Success 200",            "type": "<p>String</p> ",            "optional": false,            "field": "classes.school_name",            "description": "<p>Nom de l'établissement</p> "          },          {            "group": "Success 200",            "type": "<p>String</p> ",            "optional": false,            "field": "classes.ip",            "description": "<p>IP du serveur</p> "          }        ]      },      "examples": [        {          "title": "Success-Response:",          "content": "HTTP/1.1 200 OK\n[\n    {\"id\":1,\"name\":\"CP 1\",\"school_name\":\"Ecole Albert Camus\",\"ip\":\"127.0.0.1\"},\n    {\"id\":2,\"name\":\"CP 2\",\"school_name\":\"Ecole Albert Camus\",\"ip\":\"188.165.200.111\"}\n]",          "type": "json"        }      ]    },    "filename": "./backoffice/restapi/views.py",    "groupTitle": "Classes",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Authorization",            "description": "<p>Format : &quot;Authorization: JWT &lt;your_token&gt;&quot; : Authentification de la requête</p> "          }        ]      }    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UNAUTHORIZED",            "description": "<p>Le token n'est pas inclus dans le header ou est invalide</p> "          }        ]      },      "examples": [        {          "title": "Unauthorized:",          "content": "HTTP 401 UNAUTHORIZED\n{\n    \"detail\": \"Authentication credentials were not provided.\"\n}",          "type": "json"        }      ]    }  },  {    "type": "get",    "url": "/students/:class_id/",    "title": "Récupérer la liste des élèves d'une classe",    "version": "0.1.0",    "name": "GetStudents",    "group": "Classes",    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "<p>Object[]</p> ",            "optional": false,            "field": "students",            "description": "<p>Liste des étudiants</p> "          },          {            "group": "Success 200",            "type": "<p>Number</p> ",            "optional": false,            "field": "students.id",            "description": "<p>ID de l'étudiant</p> "          },          {            "group": "Success 200",            "type": "<p>String</p> ",            "optional": false,            "field": "student.username",            "description": "<p>Nom d'utilisateur'</p> "          }        ]      },      "examples": [        {          "title": "Success-Response:",          "content": "HTTP/1.1 200 OK\n[\n    {\"id\":11,\"username\":\"Anthony.Payet\"},\n    {\"id\":3,\"username\":\"Benjamin.Boisset\"},\n    ...\n    {\"id\":8,\"username\":\"Romain.Brunet\"}\n]",          "type": "json"        }      ]    },    "filename": "./backoffice/restapi/views.py",    "groupTitle": "Classes",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Authorization",            "description": "<p>Format : &quot;Authorization: JWT &lt;your_token&gt;&quot; : Authentification de la requête</p> "          }        ]      }    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UNAUTHORIZED",            "description": "<p>Le token n'est pas inclus dans le header ou est invalide</p> "          },          {            "group": "Error 4xx",            "optional": false,            "field": "BAD-REQUEST",            "description": "<p>Des parametres sont manquants ou invalides</p> "          }        ]      },      "examples": [        {          "title": "Unauthorized:",          "content": "HTTP 401 UNAUTHORIZED\n{\n    \"detail\": \"Authentication credentials were not provided.\"\n}",          "type": "json"        },        {          "title": "Bad-request:",          "content": "HTTP 400 BAD REQUEST",          "type": "json"        }      ]    }  },  {    "type": "get",    "url": "/exercise-config/:class_id/:reference/",    "title": "Récupérer la configuration d'un exercice",    "version": "0.1.0",    "name": "GetExerciseConfig",    "group": "Configuration",    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "<p>Number</p> ",            "optional": false,            "field": "id",            "description": "<p>ID de la configuration</p> "          },          {            "group": "Success 200",            "type": "<p>String</p> ",            "optional": false,            "field": "name",            "description": "<p>Nom de la configuration</p> "          },          {            "group": "Success 200",            "type": "<p>Object</p> ",            "optional": false,            "field": "data",            "description": "<p>Json de configuration</p> "          },          {            "group": "Success 200",            "type": "<p>String</p> ",            "optional": false,            "field": "reference",            "description": "<p>Référence de l'exercice'</p> "          }        ]      },      "examples": [        {          "title": "Success-Response:",          "content": "HTTP/1.1 200 OK\n{\n    \"id\":1,\n    \"name\":\"Config anglais lecture bloqué\",\n    \"data\":\"{\\\"accessible\\\": false, \\\"config_name\\\": \\\"Config anglais lecture bloqué\\\", \\\"school_class\\\": \\\"2\\\"}\",\n    \"reference\":\"en-lecture\"\n}",          "type": "json"        }      ]    },    "filename": "./backoffice/restapi/views.py",    "groupTitle": "Configuration",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Authorization",            "description": "<p>Format : &quot;Authorization: JWT &lt;your_token&gt;&quot; : Authentification de la requête</p> "          }        ]      }    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UNAUTHORIZED",            "description": "<p>Le token n'est pas inclus dans le header ou est invalide</p> "          },          {            "group": "Error 4xx",            "optional": false,            "field": "BAD-REQUEST",            "description": "<p>Des parametres sont manquants ou invalides</p> "          }        ]      },      "examples": [        {          "title": "Unauthorized:",          "content": "HTTP 401 UNAUTHORIZED\n{\n    \"detail\": \"Authentication credentials were not provided.\"\n}",          "type": "json"        },        {          "title": "Bad-request:",          "content": "HTTP 400 BAD REQUEST",          "type": "json"        }      ]    }  },  {    "type": "get",    "url": "/subject-config/:class_id/:reference/",    "title": "Récupérer la configuration d'une matière",    "version": "0.1.0",    "name": "GetSubjectConfig",    "group": "Configuration",    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "<p>Number</p> ",            "optional": false,            "field": "id",            "description": "<p>ID de la configuration</p> "          },          {            "group": "Success 200",            "type": "<p>String</p> ",            "optional": false,            "field": "name",            "description": "<p>Nom de la configuration</p> "          },          {            "group": "Success 200",            "type": "<p>Object</p> ",            "optional": false,            "field": "data",            "description": "<p>Json de configuration</p> "          },          {            "group": "Success 200",            "type": "<p>String</p> ",            "optional": false,            "field": "reference",            "description": "<p>Référence de la matière</p> "          }        ]      },      "examples": [        {          "title": "Success-Response:",          "content": "HTTP/1.1 200 OK\n{\n    \"id\":1,\n    \"name\":\"Anglais bloqué\",\n    \"data\":\"{\\\"accessible\\\": false, \\\"config_name\\\": \\\"Anglais bloqué\\\", \\\"school_class\\\": \\\"2\\\"}\",\n    \"reference\":\"en\"\n}",          "type": "json"        }      ]    },    "filename": "./backoffice/restapi/views.py",    "groupTitle": "Configuration",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Authorization",            "description": "<p>Format : &quot;Authorization: JWT &lt;your_token&gt;&quot; : Authentification de la requête</p> "          }        ]      }    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UNAUTHORIZED",            "description": "<p>Le token n'est pas inclus dans le header ou est invalide</p> "          },          {            "group": "Error 4xx",            "optional": false,            "field": "BAD-REQUEST",            "description": "<p>Des parametres sont manquants ou invalides</p> "          }        ]      },      "examples": [        {          "title": "Unauthorized:",          "content": "HTTP 401 UNAUTHORIZED\n{\n    \"detail\": \"Authentication credentials were not provided.\"\n}",          "type": "json"        },        {          "title": "Bad-request:",          "content": "HTTP 400 BAD REQUEST",          "type": "json"        }      ]    }  },  {    "type": "post",    "url": "/save-exercise-stat/",    "title": "Sauvegarder une statistique",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "<p>String</p> ",            "optional": false,            "field": "reference",            "description": "<p>Reference de l'exercice</p> "          },          {            "group": "Parameter",            "type": "<p>Number</p> ",            "optional": false,            "field": "user_id",            "description": "<p>ID de l'utilisateur</p> "          },          {            "group": "Parameter",            "type": "<p>String</p> ",            "optional": false,            "field": "data",            "description": "<p>Statistiques au format JSON string</p> "          }        ]      }    },    "version": "0.1.0",    "name": "PostExerciseStat",    "group": "Statistiques",    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "<p>String</p> ",            "optional": false,            "field": "result",            "description": "<p>Resultat</p> "          }        ]      },      "examples": [        {          "title": "Success-Response:",          "content": "HTTP/1.1 200 OK\n{\n    \"result\":\"success\"\n}",          "type": "json"        }      ]    },    "filename": "./backoffice/restapi/views.py",    "groupTitle": "Statistiques",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Authorization",            "description": "<p>Format : &quot;Authorization: JWT &lt;your_token&gt;&quot; : Authentification de la requête</p> "          }        ]      }    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UNAUTHORIZED",            "description": "<p>Le token n'est pas inclus dans le header ou est invalide</p> "          },          {            "group": "Error 4xx",            "optional": false,            "field": "BAD-REQUEST",            "description": "<p>Des parametres sont manquants ou invalides</p> "          }        ]      },      "examples": [        {          "title": "Unauthorized:",          "content": "HTTP 401 UNAUTHORIZED\n{\n    \"detail\": \"Authentication credentials were not provided.\"\n}",          "type": "json"        },        {          "title": "Bad-request:",          "content": "HTTP 400 BAD REQUEST",          "type": "json"        }      ]    }  }] });
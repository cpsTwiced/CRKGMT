#쿠키런: 킹덤 - Guild Member Management

## About
This program is a management tool for Cookie Run: Kingdom's guild.

## Commands to run if not working in current environment
`python -m pip install pysimplegui`

## NOTE
- If you are running the code using venv, you need to install
the following packages: PySimpleGUI
  

## members.json
`members.json` file stores the current guild members and their properties in
a specific structure.

```
{"Guild": {"name": ,
           "members": [{"name": ,
                        "activityPoint": ,
                        "damagePoint": },
                       {"name": ,
                        "activityPoint": ,
                        "damagePoint": },...]
           }
}
```

For initial UI ideas, please refer to `crkui.png`.
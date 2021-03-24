from myweb.core.runner import Runner



if __name__ == '__main__':
    config_path = "demo.json"
    r = Runner(config_name=config_path)
    r.run()
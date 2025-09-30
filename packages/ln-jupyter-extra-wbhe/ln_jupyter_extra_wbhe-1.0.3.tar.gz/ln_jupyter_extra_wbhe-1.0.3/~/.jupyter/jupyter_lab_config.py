c.ServerApp.base_url = '/jupyter/a17202855459155968362488'
c.ServerApp.port = 8888
c.ServerApp.open_browser = False

# 完全禁用所有 Anaconda 扩展
c.ServerApp.nbserver_extensions = {
    'aext_assistant_server': False,
    'aext_core_server': False,
    'aext_profile_manager_server': False,
    'aext_panels': False,
    'aext_share_notebook_server': False,
    'aext_toolbox': False,
    'aext_events_server': False,
    'aext_project_filebrowser_server': False
}

c.LabApp.extensions = {
    'aext_assistant': False,
    'aext_core': False,
    'aext_panels': False,
    'aext_share_notebook': False,
    'aext_toolbox': False
}

# 禁用自动加载扩展
c.ServerApp.autoreload = False

# 只启用必要的扩展
c.ServerApp.jpserver_extensions = {
    'jupyterlab': True,
    'notebook': True
}
import { Widget } from '@lumino/widgets';
import { listIcon } from '@jupyterlab/ui-components';
import { JupyterFrontEnd } from '@jupyterlab/application';
import { getProjectVersionList } from '../api/project';
import { createRoot } from 'react-dom/client';
import { VersionList } from '../components/VersionList';
import type { IVersion } from '../types';
import React from 'react';

class VersionListSidebarWidget extends Widget {
  private listContainer: HTMLElement; // 定义 listContainer 为类的属性
  params: any;
  _app: JupyterFrontEnd;
  _notebookProjectId: string;
  constructor(app: JupyterFrontEnd, notebookProjectId: string) {
    super();
    this._app = app;
    this._notebookProjectId = notebookProjectId;
    this.addClass('ln-version-list-sidebar'); // 使用 ln- 前缀
    this.id = 'ln-version-list-sidebar';
    this.title.caption = '版本';
    this.title.label = '版本';
    this.title.icon = listIcon;
    this.title.closable = true; // 允许关闭

    // 创建列表容器
    this.listContainer = document.createElement('div');
    this.listContainer.className = 'ln-version-list';
    this.node.appendChild(this.listContainer);

    this.params = {
      searchKey: '',
      pageSize: 15,
      pageNum: 1,
      tagLabels: [],
      sortType: 'deployTime'
    };

    // 调用获取版本的函数
    this.getVersions(notebookProjectId);
  }

  async getVersions(notebookProjectId: string) {
    const params = {
      notebookId: notebookProjectId || '',
      pageSize: 1,
      pageNum: 1
    };
    try {
      const res = await getProjectVersionList(params);
      const list = res.list;
      this.updateVersionList(list); // 更新版本列表
    } catch (error) {
      console.error('Failed to fetch versions:', error);
    }
  }

  updateVersionList(data: IVersion[]) {
    this.listContainer.innerHTML = '';
    const versions = data || [];
    // 确保正确处理空数组情况
    if (versions.length === 0) {
      this.listContainer.innerHTML =
        '<div style="width:100%;text-align:center;margin-top:20px">暂无版本</div>';
      return;
    }

    // 使用 createRoot 替代 ReactDOM.render（推荐）
    const root = createRoot(this.listContainer);
    root.render(
      <div>
        {versions.map(version => (
          <VersionList
            key={version.version} // 使用唯一 key
            id={version.id}
            version={version.version}
            createTime={version.createTime}
            app={this._app}
            projectId={this._notebookProjectId}
          />
        ))}
      </div>
    );
  }

  install(app: JupyterFrontEnd) {
    app.shell.add(this, 'left', {
      rank: 900,
      type: 'tab'
    });
  }
}

export default VersionListSidebarWidget;

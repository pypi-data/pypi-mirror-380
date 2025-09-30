import { JupyterFrontEnd } from '@jupyterlab/application';
import { Notification } from '@jupyterlab/apputils';
import { saveIcon } from '@jupyterlab/ui-components';
import { CommandToolbarButton } from '@jupyterlab/apputils';
import React from 'react';
import { createRoot } from 'react-dom/client';
import { addProjectVersion, submitStudentWork } from '../api/project';
import VersionListSidebarWidget from './version';
// 版本创建表单组件
const VersionCreationForm: React.FC<{
  onClose: () => void;
  onSubmit: () => Promise<void>;
  roleType: number;
}> = ({ onClose, onSubmit, roleType }) => {
  const [loading, setLoading] = React.useState(false);
  // const [formData, setFormData] = useState({
  //   name: '',
  //   description: ''
  // });
  // const [errors, setErrors] = useState({
  //   name: '',
  //   description: ''
  // });

  // // 校验版本名称
  // const validateName = (name: string) => {
  //   const nameRegex = /^[a-zA-Z0-9.]+$/;
  //   if (!name) {
  //     return '版本名称不能为空';
  //   }
  //   if (name.length > 10) {
  //     return '版本名称长度不能超过10个字符';
  //   }
  //   if (!nameRegex.test(name)) {
  //     return '版本名称只能包含英文、数字和.';
  //   }
  //   return '';
  // };

  // // 校验描述
  // const validateDescription = (description: string) => {
  //   if (description.length > 300) {
  //     return '版本描述不能超过300个字符';
  //   }
  //   return '';
  // };

  // 处理输入变化
  // const handleChange = (
  //   e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  // ) => {
  //   const { name, value } = e.target;
  //   setFormData(prev => ({
  //     ...prev,
  //     [name]: value
  //   }));
  // };

  // 提交表单
  const handleSubmit = async () => {
    // const nameError = validateName(formData.name);
    // const descriptionError = validateDescription(formData.description);

    // // 设置错误信息
    // setErrors({
    //   name: nameError,
    //   description: descriptionError
    // });

    // // 如果有错误，阻止提交
    // if (nameError || descriptionError) {
    //   return;
    // }
    setLoading(true);
    try {
      // 调用提交接口
      await onSubmit();
      Notification.success(
        `${roleType === 1 ? '公开版本成功' : '提交作业成功'}`,
        { autoClose: 3000 }
      );
      setLoading(false);
      // 成功后关闭弹框
      onClose();
    } catch (error) {
      setLoading(false);
      console.error('提交失败', error);
    }
  };

  React.useEffect(() => {
    const style = document.createElement('style');
    style.innerHTML = `
      @keyframes spin {
        0% { transform: rotate(0deg);}
        100% { transform: rotate(360deg);}
      }
    `;
    document.head.appendChild(style);
    return () => {
      document.head.removeChild(style);
    };
  }, []);

  return (
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        zIndex: 1000
      }}
    >
      <div
        style={{
          backgroundColor: 'white',
          padding: '20px',
          borderRadius: '8px',
          boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
          width: '300px'
        }}
      >
        <h2 style={{ marginTop: 0, marginBottom: '20px', textAlign: 'center' }}>
          是否{roleType === 1 ? '公开' : '提交作业'}?
        </h2>

        <div style={{ marginBottom: '15px' }}>
          {/* <label
            style={{
              display: 'block',
              marginBottom: '5px',
              fontWeight: 'bold'
            }}
          >
            版本名称
          </label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="请输入版本名称（英文、数字、点，最长10字符）"
            style={{
              width: '100%',
              padding: '8px',
              boxSizing: 'border-box',
              borderColor: errors.name ? 'red' : '#ccc',
              borderWidth: '1px',
              borderStyle: 'solid'
            }}
          />
          {errors.name && (
            <p style={{ color: 'red', margin: '5px 0 0' }}>{errors.name}</p>
          )} */}
        </div>

        <div>
          {/* <label
            style={{
              display: 'block',
              marginBottom: '5px',
              fontWeight: 'bold'
            }}
          >
            版本描述
          </label>
          <textarea
            name="description"
            value={formData.description}
            onChange={handleChange}
            placeholder="请输入版本描述（最长300字符）"
            style={{
              width: '100%',
              padding: '8px',
              boxSizing: 'border-box',
              minHeight: '100px',
              borderColor: errors.description ? 'red' : '#ccc',
              borderWidth: '1px',
              borderStyle: 'solid'
            }}
          />
          {errors.description && (
            <p style={{ color: 'red', margin: '5px 0 0' }}>
              {errors.description}
            </p>
          )} */}
        </div>

        <div
          style={{
            display: 'flex',
            justifyContent: 'center',
            marginTop: '20px'
          }}
        >
          <button
            onClick={onClose}
            style={{
              padding: '8px 16px',
              marginRight: '28px',
              backgroundColor: '#f0f0f0',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer'
            }}
          >
            取消
          </button>
          <button
            onClick={handleSubmit}
            style={{
              padding: '8px 16px',
              backgroundColor: '#4194fc',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: loading ? 'not-allowed' : 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}
            disabled={loading}
          >
            {loading && (
              <span
                style={{
                  width: 16,
                  height: 16,
                  border: '2px solid #fff',
                  borderTop: '2px solid #4194fc',
                  borderRadius: '50%',
                  marginRight: 8,
                  display: 'inline-block',
                  animation: 'spin 1s linear infinite'
                }}
              />
            )}
            {loading ? '加载中...' : '确定'}
          </button>
        </div>
      </div>
    </div>
  );
};

class SaveButton extends CommandToolbarButton {
  private dialogContainer: HTMLDivElement | null = null;
  private dialogRoot: ReturnType<typeof createRoot> | null = null;
  private _app: JupyterFrontEnd;
  notebookProjectId: string;
  teachingId: string;
  originVersionId: string;
  roleType: number;
  constructor(
    app: JupyterFrontEnd,
    notebookProjectId: string,
    teachingId: string,
    roleType: number,
    originVersionId: string
  ) {
    const COMMAND_ID = 'version:create';
    app.commands.addCommand(COMMAND_ID, {
      label: roleType === 1 ? '公开' : '提交作业',
      icon: saveIcon,
      execute: () => {
        this.handleSave(
          app,
          notebookProjectId,
          teachingId,
          roleType,
          originVersionId
        );
      }
    });

    super({
      commands: app.commands,
      id: COMMAND_ID
    });

    this.id = 'version-list-save-button';
    this._app = app;
    this.notebookProjectId = notebookProjectId;
    this.teachingId = teachingId;
    this.roleType = roleType;
    this.originVersionId = originVersionId;
    this.node.classList.add('custom-save-button');
  }

  install(app: JupyterFrontEnd): void {
    app.shell.add(this, 'top', {
      rank: 1000
    });
  }

  private handleSave(
    app: JupyterFrontEnd,
    notebookProjectId: string,
    teachingId: string,
    roleType: number,
    originVersionId: string
  ): void {
    // 创建对话框容器
    this.dialogContainer = document.createElement('div');
    document.body.appendChild(this.dialogContainer);

    // 创建 React 根
    this.dialogRoot = createRoot(this.dialogContainer);

    const closeDialog = () => {
      if (this.dialogRoot && this.dialogContainer) {
        this.dialogRoot.unmount();
        document.body.removeChild(this.dialogContainer);
        this.dialogContainer = null;
        this.dialogRoot = null;
      }
    };

    const submitVersion = async () => {
      const api = roleType === 1 ? addProjectVersion : submitStudentWork;
      const params =
        this.roleType === 1
          ? {
              originVersionId,
              originTeachingId: teachingId || '',
              version: ''
            }
          : {
              notebookId: notebookProjectId || '',
              teachingId,
              originVersionId,
              workVersion: ''
            };
      try {
        await api(params);
        this.refreshData(this._app);
      } catch (error) {
        console.error('版本创建失败:', error);
      }
    };

    // 渲染对话框
    this.dialogRoot.render(
      <VersionCreationForm
        onClose={closeDialog}
        onSubmit={submitVersion}
        roleType={this.roleType}
      />
    );
  }

  private refreshData(app: JupyterFrontEnd): void {
    const widgets = Array.from(app.shell.widgets('left'));
    console.log(widgets);
    const versionListWidget = widgets.find(
      widget => widget.id === 'ln-version-list-sidebar'
    );
    if (versionListWidget) {
      // 直接调用 getVersions 方法刷新列表
      (versionListWidget as VersionListSidebarWidget).getVersions(
        this.notebookProjectId
      );
    }
  }
}

export default SaveButton;

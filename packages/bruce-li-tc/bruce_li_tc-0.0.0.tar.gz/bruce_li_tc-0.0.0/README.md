# Bruce Li TC

�߼�Python���߿⣬�ṩ΢���Զ�����ʱ������ݴ����ܡ�

## ��������

- ? ΢����Ƶ�Զ�������
- ? �߼�ʱ�䴦����
- ? ���ݷ����ʹ���
- ? ������������ݿ����
- ? ͼ����ͼ�����Ӿ�

## ��װ

```bash
pip install bruce-li-tc
```
## Ŀ¼�ṹ
```
Bruce_li_tc/                          # ?? ��Ŀ��Ŀ¼����ͨ�ļ��У�
������ .github/                          # ?? GitHub����Ŀ¼����ͨ�ļ��У�
��   ������ workflows/                    # ?? GitHub Actions����������ͨ�ļ��У�
��       ������ ci.yml                    # ? CI���������ļ�
��       ������ release.yml               # ? �Զ����������ļ�
������ src/                              # ?? Դ����Ŀ¼����ͨ�ļ��У�
��   ������ bruce_li_tc/                  # ?? Python��Ŀ¼��Python����������__init__.py��
��       ������ __init__.py               # ? ����ʼ���ļ���Python����ʶ��
��       ������ _version.py               # ? �汾�����ļ����ᱻsetuptools-scm���ǣ�
��       ������ wechatauto/               # ?? ΢���Զ���ģ�飨Python�Ӱ���
��       ��   ������ __init__.py           # ? �Ӱ���ʼ���ļ�
��       ��   ������ wechat_video_automator/
��       ��       ������ bruce_uiauto/     # ?? ��Դ�ļ�Ŀ¼
��       ������ network/                  # ?? ���繤��ģ�飨Python�Ӱ���
��           ������ __init__.py           # ? �Ӱ���ʼ���ļ�
��           ������ ...                   # ��������ģ���ļ�
������ tests/                            # ?? ����Ŀ¼����ͨ�ļ��У�
��   ������ __init__.py                   # ? ���԰���ʼ���ļ�
������ scripts/                          # ?? �ű�Ŀ¼����ͨ�ļ��У�
��   ������ update_version.py             # ? �汾���½ű�
��   ������ test_before_release.py        # ? ����ǰ���Խű�
������ venv/                             # ?? ���⻷����.gitignore���ԣ�
������ dist/                            # ?? ���������.gitignore���ԣ�
������ .gitignore                       # ? Git���Թ���
������ pyproject.toml                   # ? ��Ŀ��������
������ requirements.txt                 # ? ��Ŀ����
������ requirements-dev.txt             # ? ��������
������ CHANGELOG.md                     # ? �����־��Ҳ�ǵ�ǰREADME��
������ README.md                        # ? ��Ŀ�����ĵ���������
```
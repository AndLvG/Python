import shutil
"""
����������,�������,���������� �������� 
��������� ���������� ������ shutil
"""
# ������� ��� ������ ���������
shutil.rmtree("D:\\path")

# ����������� ����� ������ ���������
shutil.copytree("D:\\Source",
               "D:\\Destination")

# ����������� ����� ���� ��� �������
shutil.move("D:\\Source",
               "D:\\Destination")
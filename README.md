# secretproject

Em sửa lại code để chạy trên cả linux và windows.

## Code
Logic thay đổi 1 chút.
- commond.py

  Không sử dụng TO_DATE nữa mà dùng request days. Là số ngày tiếp theo mình muốn request
  
 - pull_request.py

  Thay đổi logic để request tới ngày khác. Thay vì tạo ra nhiều url, em tìm button ngày kế và thêm sự kiện click_next() cho nó
  
 - Cần cải thiện sau

  Xóa pandas và thay bằng function đơn giản hơn để export data nhanh hơn

## Environment
- Chạy trên windows thì anh chạy như bình thường, python pull_vnairline.py
- Chạy trên centos, sau khi cài xong như trong hướng dẫn. chạy câu lệnh như bên dưới : 
  
  export DISPLAY=localhost:1.0; python3.6 pull_vnairline.py

## Document
- Tài liệu hướng dẫn cài Selenium trên Centos 7, hiện tại em mới chỉ cài ở máy ảo của em
- Tài liệu hướng dẫn cài python 2.7, anh có cài nhớ cài 3.6 nha, để sửa lại tài liệu sau

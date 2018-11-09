# secretproject

Em sửa lại code để chạy trên cả linux và windows.

## Code
Logic thay đổi 1 chút.
- commond.py

  Không sử dụng TO_DATE nữa mà dùng request days. Là số ngày tiếp theo mình muốn request
  
 - pull_request.py
 
  Thay vì general ra n url tương ứng với n ngày. Em đi kiếm button ngày kiếm theo rồi xử lý sự kiện click để nó tự động next qua ngày khác.
  
 - Cần cải thiện sau
 
  Xóa pandas và thay bằng function đơn giản hơn để export data nhanh hơn

## Environment
- Chạy trên windows thì anh chạy như bình thường, python pull_vnairline.py
- Chạy trên centos, sau khi cài xong như trong hướng dẫn. chạy câu lệnh như bên dưới : 
  
  export DISPLAY=localhost:1.0; python3.6 pull_vnairline.py

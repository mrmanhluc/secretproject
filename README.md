# secretproject

Em sửa lại code để chạy trên cả linux và windows.

Logic thay đổi 1 chút.
- commond.py
  Không sử dụng TO_DATE nữa mà dùng request days. Là số ngày tiếp theo mình muốn request
  
 - pull_request
  Thay vì general ra n url tương ứng với n ngày. Em đi kiếm button ngày kiếm theo rồi xử lý sự kiện click để nó tự động next qua ngày khác.
  
 - Cần cải thiện sau
  Xóa pandas và thay bằng function đơn giản hơn để export data nhanh hơn

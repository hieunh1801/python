# Factory Pattern: quản lý và trả về đối tượng theo yêu cầu.

Cài đặt: Factory Pattern

- __Super Class:__ 
    - có thể là interface, abstract hay một class thông thường
    - nhiệm vụ: đóng vai trò là lớp cha chung cho các thằng con
- __Sub Class:__
    - sub class implement lại các method của super class  
- __Factory Class:__
    - chịu trách nhiệm khởi tạo đối tượng sub class theo tham số đầu vào
    - thường sử dụng if - else để xác định đầu vào

Ví dụ: 
- Các ngân hàng cung cấp các API để truy cập tới hệ thống của họ
- Nhiệm vụ của bạn: xây dựng một API để client có thể sử dụng được một dịch vụ của ngân hàng bất kì. 
- Hiện trong hệ thống của bạn mới chỉ có __TPBank__, __VietcomBank__. Nếu code chay => mỗi khi client truy vấn tới cái nào thì ta if else => rất mất công sức. Khi thêm một hệ thống mới => khó bảo trì. Vì vậy ta sử dụng Factory Pattern để xây dựng module chung => OK

```java
// Super class
public interface Bank {
    String getBankName();
}


// Sub class - TPBank
public class TPBank implements Bank {
    @Override
    public String getBankName() {
        return "TPBank";
    }
}

// Sub class - VietcomBank
public class VietcomBank implements Bank {
    @Override
    public String getBankName() {
        return "VietcomBank";
    }
}

// FactoryClass
public class BankFactory {
    private BankFactory() { }
    public static final Bank getBank(BankType bankType) {
        switch (bankType) {
        case TPBANK:
            return new TPBank();
        case VIETCOMBANK:
            return new VietcomBank();
        default:
            throw new IllegalArgumentException("This bank type is unsupported");
        }
    }
}

// Bank Type => để select ra bank
public enum BankType {
    VIETCOMBANK, TPBANK;
}

// Client - gọi các API tương ứng từ bank họ cần
public class Client {
    public static void main(String[] args) {
        Bank bank = BankFactory.getBank(BankType.TPBANK);
        System.out.println(bank.getBankName()); // TPBank
    }
}
```

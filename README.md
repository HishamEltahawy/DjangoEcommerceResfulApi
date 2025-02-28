# Django Ecommerce RESTful API Documentation

## Overview
هذا المشروع هو **واجهة برمجية RESTful** لمنصة **التجارة الإلكترونية** مبنية باستخدام **Django** و **Django REST Framework**، ويشمل الميزات التالية:
- تسجيل المستخدمين وتوثيقهم
- إدارة المنتجات
- معالجة الطلبات
- والمزيد...

---

## 📂 Project Structure
```
DjangoEcommerceResfulApi/
├── AccountsApp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── OrdersApp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── ProductsApp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── ProjectFiles/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

---

## 🚀 Installation

1. **استنساخ المستودع:**
```sh
git clone https://github.com/yourusername/DjangoEcommerceResfulApi.git
cd DjangoEcommerceResfulApi
```

2. **إنشاء البيئة الافتراضية وتفعيلها:**
```sh
python -m venv venv
venv\Scripts\activate  # على Windows
source venv/bin/activate  # على macOS/Linux
```

3. **تثبيت المتطلبات:**
```sh
pip install -r requirements.txt
```

4. **تطبيق الترحيلات:**
```sh
python manage.py migrate
```

5. **إنشاء مستخدم مدير:**
```sh
python manage.py createsuperuser
```

6. **تشغيل خادم التطوير:**
```sh
python manage.py runserver
```

---

## 📌 API Endpoints

### 📌 AccountsApp
#### 🟢 User Registration
- **URL:** `/api/accounts/register/`
- **Method:** `POST`
- **Description:** تسجيل مستخدم جديد.
- **Request Body:**
```json
{
  "username": "string",
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "password": "string"
}
```
- **Response:**
```json
{
  "details": "Add User Successful"
}
```

#### 🔵 Forget Password
- **URL:** `/api/accounts/forget_password/`
- **Method:** `POST`
- **Description:** إرسال رابط إعادة تعيين كلمة المرور إلى البريد الإلكتروني.

#### 🟡 Reset Password
- **URL:** `/api/accounts/reset_password/<token>/`
- **Method:** `POST`
- **Description:** إعادة تعيين كلمة المرور باستخدام التوكن.

### 📌 OrdersApp
#### 🟢 Get All Orders
- **URL:** `/api/orders/`
- **Method:** `GET`
- **Description:** استرجاع جميع الطلبات.

#### 🔵 Get One Order
- **URL:** `/api/orders/<pk>/`
- **Method:** `GET`
- **Description:** استرجاع طلب معين باستخدام **ID**.

#### 🟡 Process Order
- **URL:** `/api/orders/<pk>/process/`
- **Method:** `PUT`
- **Description:** تحديث حالة الطلب.

#### 🔴 Delete Order
- **URL:** `/api/orders/<pk>/`
- **Method:** `DELETE`
- **Description:** حذف طلب معين.

#### 🟢 Create New Order
- **URL:** `/api/orders/new/`
- **Method:** `POST`
- **Description:** إنشاء طلب جديد.

### 📌 ProductsApp
#### 🟢 Get All Products
- **URL:** `/api/products/`
- **Method:** `GET`
- **Description:** استرجاع جميع المنتجات.

#### 🔵 Get One Product
- **URL:** `/api/products/<pk>/`
- **Method:** `GET`
- **Description:** استرجاع منتج معين باستخدام **ID**.

#### 🟢 Create New Product
- **URL:** `/api/products/new/`
- **Method:** `POST`
- **Description:** إنشاء منتج جديد.

#### 🟡 Update Product
- **URL:** `/api/products/<pk>/`
- **Method:** `PUT`
- **Description:** تحديث منتج موجود.

#### 🔴 Delete Product
- **URL:** `/api/products/<pk>/`
- **Method:** `DELETE`
- **Description:** حذف منتج معين.

---

## 🛠 Models

### 📌 AccountsApp
#### Profile
- `user`: `ForeignKey(User)`
- `new_token`: `CharField`
- `ex_date`: `DateTimeField`

### 📌 OrdersApp
#### Order
- `user`: `ForeignKey(User)`
- `city`: `CharField`
- `zip_code`: `CharField`
- `street`: `CharField`
- `phone_no`: `CharField`
- `country`: `CharField`
- `total_amount`: `FloatField`
- `status`: `CharField`
- `created_at`: `DateTimeField`
- `updated_at`: `DateTimeField`

#### OrderItem
- `product`: `ForeignKey(Product)`
- `order`: `ForeignKey(Order)`
- `name`: `CharField`
- `quantity`: `IntegerField`
- `price`: `FloatField`

### 📌 ProductsApp
#### Product
- `name`: `CharField`
- `description`: `TextField`
- `price`: `FloatField`
- `stock`: `IntegerField`
- `created_at`: `DateTimeField`
- `updated_at`: `DateTimeField`

---

## 🔐 Permissions
- `IsAuthenticated`: يضمن أن المستخدم **مسجل الدخول**.
- `IsAdminUser`: يضمن أن المستخدم **مشرف**.

---

## 📢 Conclusion
هذا التوثيق يوفر نظرة شاملة على **Django Ecommerce RESTful API**، بما في ذلك:
- تثبيت المشروع
- نقاط النهاية **(API Endpoints)**
- النماذج **(Models)**
- المتسلسلات **(Serializers)**
- الأذونات **(Permissions)**

إذا كنت بحاجة إلى أي استفسارات أو دعم، لا تتردد في التواصل! 🚀

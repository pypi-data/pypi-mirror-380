#!/usr/bin/env python3
"""
演示参数冲突问题
"""

def demo_parameter_conflict():
    """演示参数冲突问题"""
    print("🔍 参数冲突问题演示")
    print("=" * 50)
    
    # 模拟requests.Session.post方法
    class MockSession:
        def post(self, url, data=None, json=None, **kwargs):
            print(f"MockSession.post called with:")
            print(f"  url: {url}")
            print(f"  data: {data}")
            print(f"  json: {json}")
            print(f"  kwargs: {kwargs}")
            return "success"
    
    # 错误的实现
    class BadHTTPClient:
        def post(self, url, data=None, json_data=None, **kwargs):
            session = MockSession()
            print("\n❌ 错误实现:")
            print(f"调用: client.post(url, json=data)")
            print(f"内部传递: session.post(url, data=data, json=json_data, **kwargs)")
            
            # 这里会出问题，因为调用时传递了json=data
            # 但函数内部又传递了json=json_data
            try:
                # 模拟调用时传递json=data的情况
                result = session.post(url, data=data, json=json_data, json=data)  # 重复的json参数
                return result
            except TypeError as e:
                print(f"错误: {e}")
                return None
    
    # 正确的实现
    class GoodHTTPClient:
        def post(self, url, data=None, json=None, **kwargs):
            session = MockSession()
            print("\n✅ 正确实现:")
            print(f"调用: client.post(url, json=data)")
            print(f"内部传递: session.post(url, data=data, json=json, **kwargs)")
            
            # 这里不会出问题，因为参数名一致
            result = session.post(url, data=data, json=json, **kwargs)
            return result
    
    # 测试
    print("测试数据:")
    test_data = {"message": "Hello", "value": 123}
    print(f"test_data: {test_data}")
    
    # 测试错误实现
    bad_client = BadHTTPClient()
    bad_result = bad_client.post("http://example.com", json=test_data)
    
    # 测试正确实现
    good_client = GoodHTTPClient()
    good_result = good_client.post("http://example.com", json=test_data)
    
    print(f"\n结果:")
    print(f"错误实现结果: {bad_result}")
    print(f"正确实现结果: {good_result}")

def demo_requests_behavior():
    """演示requests库的实际行为"""
    print("\n🔍 requests库行为演示")
    print("=" * 50)
    
    try:
        import requests
        
        # 创建一个模拟的requests.Session
        class MockRequestsSession:
            def post(self, url, data=None, json=None, **kwargs):
                print(f"requests.Session.post called with:")
                print(f"  url: {url}")
                print(f"  data: {data}")
                print(f"  json: {json}")
                print(f"  kwargs: {kwargs}")
                return "MockResponse"
        
        session = MockRequestsSession()
        
        # 正确的调用
        print("\n✅ 正确的调用:")
        result1 = session.post("http://example.com", json={"test": "data"})
        print(f"结果: {result1}")
        
        # 错误的调用（会导致参数冲突）
        print("\n❌ 错误的调用（模拟）:")
        try:
            # 这会导致TypeError: got multiple values for keyword argument 'json'
            result2 = session.post("http://example.com", json={"test": "data"}, json={"another": "value"})
        except TypeError as e:
            print(f"错误: {e}")
        
    except ImportError:
        print("requests库未安装，跳过实际测试")

if __name__ == "__main__":
    demo_parameter_conflict()
    demo_requests_behavior()

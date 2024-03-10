import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  runApp(
    const MaterialApp(
      home: MyApp(),
    ),
  );
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> with SingleTickerProviderStateMixin {
  late WebViewController controller;
  late TabController _tabController;
  int _selectedIndex = 0;

  @override
  void initState() {
    super.initState();
    controller = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..loadRequest(Uri.parse('https://www.google.com'));

    _tabController = TabController(length: 5, vsync: this);
    _tabController.addListener(() {
      setState(() {
        _selectedIndex = _tabController.index;
      });
    });
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  void pressHome() {
    controller.loadRequest(
      Uri.parse('https://www.google.com'),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 50,
        title: const Text(
          '대충 로고자리',
          style: TextStyle(
            fontWeight: FontWeight.bold,
            fontSize: 30,
          ),
        ),
        backgroundColor: Colors.white,
        actions: [
          IconButton(
            onPressed: () {},
            icon: const Icon(Icons.search),
          ),
          IconButton(
            onPressed: () {},
            icon: const Icon(Icons.notifications),
          ),
        ],
      ),
      body: WebViewWidget(
        controller: controller,
      ),
      bottomNavigationBar: SizedBox(
        height: 70,
        child: TabBar(
          controller: _tabController,
          onTap: (index) {
            setState(() {
              _selectedIndex = index;
            });

            if (_selectedIndex == 0) {
              // "Home" 탭을 눌렀을 때의 동작
              pressHome();
            }
          },
          tabs: const <Widget>[
            Tab(
              icon: Icon(
                Icons.home,
                color: Colors.black,
              ),
            ),
            Tab(
              icon: Icon(
                Icons.text_format_sharp,
                color: Colors.black,
              ),
            ),
            Tab(
              icon: Icon(
                Icons.circle_outlined,
                color: Colors.blue,
                size: 50,
              ),
            ),
            Tab(
              icon: Icon(
                Icons.article,
                color: Colors.black,
              ),
            ),
            Tab(
              icon: Icon(
                Icons.account_circle_outlined,
                color: Colors.black,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

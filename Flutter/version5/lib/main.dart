import 'package:flutter/material.dart';
import 'package:flutter_inappwebview/flutter_inappwebview.dart';

void main() {
  runApp(
    const MaterialApp(
      home: MyHomePage(),
    ),
  );
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: InAppWebView(
        initialUrlRequest: URLRequest(url: Uri.parse("http://10.0.2.2:5173/")),
        onWebViewCreated: (controller) {
          controller.addJavaScriptHandler(
              handlerName: 'Sample', callback: (args) {});
        },
        onLoadStart: (controller, url) {},
        onLoadStop: (controller, url) {},
      ),
    );
  }
}

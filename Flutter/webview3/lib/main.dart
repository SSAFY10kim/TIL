import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';
import 'package:completer_ex/completer_ex.dart';
import 'dart:async';

void main() {
  runApp(const MaterialApp(
    home: MyHomePage(),
  ));
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late WebViewController _webViewController;
  final Completer<WebViewController> _controller =
      Completer<WebViewController>();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: WebView(
        initialUrl: "http://10.0.2.2:5173/",
        javascriptMode: JavascriptMode.unrestricted,
        onWebViewCreated: (WebViewController webViewController) {
          _controller.complete(webViewController);
          _webViewController = webViewController;
        },
        javascriptChannels: <JavascriptChannel>{
          JavascriptChannel(
              name: "Sample",
              onMessageReceived: (JavascriptMessage message) {
                //필요한 처리 내용 작성
              })
        },
      ),
    );
  }
}

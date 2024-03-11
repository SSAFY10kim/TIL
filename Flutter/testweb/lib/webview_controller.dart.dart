import 'package:flutter/material.dart';
import 'package:get/get.dart'; // Get 라이브러리 추가
import 'package:webview_flutter/webview_flutter.dart';

class WebResourceError {
  final String description;
  final int errorCode;
  final String failingUrl;

  WebResourceError({
    required this.description,
    required this.errorCode,
    required this.failingUrl,
  });
} // WebResourceError에 대한 더미 클래스 추가

class WebviewMainController extends GetxController {
  static WebviewMainController get to => Get.find();

  final WebViewController controller = WebViewController()
    ..setJavaScriptMode(JavaScriptMode.unrestricted)
    ..setNavigationDelegate(
      NavigationDelegate(
        onProgress: (int progress) {
          debugPrint('progressing $progress');
        },
        onPageStarted: (String url) {
          debugPrint(url);
        },
        onPageFinished: (String url) {
          debugPrint('Page Finished');
        },
      ),
    )
    ..loadRequest(Uri.parse('http://192.168.30.111:3000'));

  WebViewController getController() {
    return controller;
  }
}

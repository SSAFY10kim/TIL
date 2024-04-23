import 'package:flutter/material.dart';

class Memo extends ChangeNotifier {
  String _memo = '';
  String get memo => _memo;

  void setMemo(String memo) {
    _memo = memo;
    notifyListeners();
  }
}

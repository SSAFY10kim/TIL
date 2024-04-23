import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:testpro/providers/counts.dart';

class Buttons extends StatelessWidget {
  const Buttons({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        ElevatedButton(
            onPressed: () {
              context.read<Counts>().add();
            },
            child: const Icon(Icons.add)),
        const SizedBox(
          width: 40,
        ),
        ElevatedButton(
            onPressed: () {
              context.read<Counts>().sub();
            },
            child: const Icon(Icons.remove))
      ],
    );
  }
}

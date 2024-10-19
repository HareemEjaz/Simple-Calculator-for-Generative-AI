{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMyznytWyfzYelCtRmUMkZ/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/HareemEjaz/Simple-Calculator-for-Generative-AI/blob/main/app4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u4HAjKOoPVgZ",
        "outputId": "2f8b812c-a635-4f99-bdcf-2e1443fee42a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Select operation:\n",
            "1. Add\n",
            "2. Subtract\n",
            "3. Multiply\n",
            "4. Divide\n",
            "Enter choice (1/2/3/4): 4\n",
            "Enter first number: 50\n",
            "Enter second number: 60\n",
            "50.0 / 60.0 = 0.8333333333333334\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "\n",
        "def add(x, y):\n",
        "    return x + y\n",
        "\n",
        "def subtract(x, y):\n",
        "    return x - y\n",
        "\n",
        "def multiply(x, y):\n",
        "    return x * y\n",
        "\n",
        "def divide(x, y):\n",
        "    if y == 0:\n",
        "        return \"Error! Division by zero.\"\n",
        "    return x / y\n",
        "\n",
        "# Streamlit UI\n",
        "st.title(\"Simple Calculator\")\n",
        "\n",
        "# Input fields\n",
        "num1 = st.number_input(\"Enter first number\", format=\"%.2f\")\n",
        "num2 = st.number_input(\"Enter second number\", format=\"%.2f\")\n",
        "\n",
        "# Operation selection\n",
        "operation = st.selectbox(\"Select operation\", [\"Add\", \"Subtract\", \"Multiply\", \"Divide\"])\n",
        "\n",
        "# Calculation and result display\n",
        "if st.button(\"Calculate\"):\n",
        "    if operation == \"Add\":\n",
        "        result = add(num1, num2)\n",
        "    elif operation == \"Subtract\":\n",
        "        result = subtract(num1, num2)\n",
        "    elif operation == \"Multiply\":\n",
        "        result = multiply(num1, num2)\n",
        "    elif operation == \"Divide\":\n",
        "        result = divide(num1, num2)\n",
        "\n",
        "    st.write(f\"The result is: {result}\")\n",
        "\n"
      ]
    }
  ]
}
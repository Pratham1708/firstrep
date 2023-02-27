{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN/dDSO+J1ly0pVJG+GxoSN",
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
        "<a href=\"https://colab.research.google.com/github/Pratham1708/firstrep/blob/main/Shopping_Bill.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E4CBVu8yq3NP",
        "outputId": "21035188-8664-4d64-c968-7fec5eb83802"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-----------SHOPPING BILL FOR STATIONERY ITEMS-----------\n",
            "Here are the items for you select which of the items you want, how many you want ? just go for it\n",
            "1.Pen:-      10Rs\n",
            "2.Paper:-     2Rs\n",
            "3.Pencil:-    5Rs\n",
            "4.Eraser:-    7Rs\n",
            "5.Book:-     25Rs\n",
            "Enter the choice no.1\n",
            "Enter how many pens do you want?:-23\n",
            "Total price for pens is:- 230\n",
            "Do you wish to continue(y/n)y\n",
            "Enter the choice no.4\n",
            "Enter how many erasers do you want?:-10\n",
            "Total price for erasers is:- 70\n",
            "Do you wish to continue(y/n)n\n",
            "------THANK YOU-------\n",
            "Total price for the stationery items is:- 300\n",
            "CGST:- 18.0 Rs\n",
            "SGST:- 18.0 Rs\n",
            "Total Price of items is:-  336.0\n",
            "Total Price of items after delivery charge is:-  436.0\n"
          ]
        }
      ],
      "source": [
        "print(\"-----------SHOPPING BILL FOR STATIONERY ITEMS-----------\")\n",
        "print(\"Here are the items for you select which of the items you want, how many you want ? just go for it\") \n",
        "print(\"1.Pen:-      10Rs\")\n",
        "print(\"2.Paper:-     2Rs\")\n",
        "print(\"3.Pencil:-    5Rs\")\n",
        "print(\"4.Eraser:-    7Rs\")\n",
        "print(\"5.Book:-     25Rs\")\n",
        "a=1\n",
        "price1,price2,price3,price4,price5=0,0,0,0,0\n",
        "while a>0:\n",
        "     choice=int(input(\"Enter the choice no.\"))\n",
        "     if choice==1:\n",
        "         num1=int(input(\"Enter how many pens do you want?:-\"))\n",
        "         price1+=num1*10\n",
        "         print(\"Total price for pens is:-\",price1)\n",
        "     elif choice==2:\n",
        "         num2=int(input(\"Enter how many papers do you want?:-\"))\n",
        "         price2+=num2*2\n",
        "         print(\"Total price for papers is:-\",price2)\n",
        "     elif choice==3:\n",
        "         num3=int(input(\"Enter how many pencils do you want?:-\"))\n",
        "         price3+=num3*5\n",
        "         print(\"Total price for pencils is:-\",price3)\n",
        "     elif choice==4:\n",
        "         num4=int(input(\"Enter how many erasers do you want?:-\"))\n",
        "         price4+=num4*7\n",
        "         print(\"Total price for erasers is:-\",price4)\n",
        "     elif choice==5:\n",
        "         num5=int(input(\"Enter how many books do you want?:-\"))\n",
        "         price5+=num5*25\n",
        "         print(\"Total price for books is:-\",price5)\n",
        "     else:\n",
        "         print(\"Invalid Choice no.\")\n",
        "     x=input(\"Do you wish to continue(y/n)\")\n",
        "     if x==\"y\":\n",
        "         continue\n",
        "     else:\n",
        "         print(\"------THANK YOU-------\")\n",
        "         a=-1\n",
        "total_price= price1+price2+price3+price4+price5\n",
        "print(\"Total price for the stationery items is:-\",total_price)\n",
        "gst=(12*total_price)/100\n",
        "sgst=gst/2\n",
        "cgst=gst/2\n",
        "print(\"CGST:-\",cgst,\"Rs\")\n",
        "print(\"SGST:-\",sgst,\"Rs\")\n",
        "Total_price=total_price+cgst+sgst\n",
        "print(\"Total Price of items is:- \",Total_price)\n",
        "delivery_charge=100\n",
        "if Total_price<500:\n",
        "    print(\"Total Price of items after delivery charge is:- \",Total_price+delivery_charge)\n",
        "else:\n",
        "    print(\"Total Price of items is:- \",Total_price)\n",
        "# This program is written by Pratham Jindal\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Ll-Ee8jJq_rf"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
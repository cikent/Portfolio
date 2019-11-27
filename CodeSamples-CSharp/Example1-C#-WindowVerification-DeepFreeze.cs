using System;
using System.Threading;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
using System.Windows.Forms;

namespace DeepFreezeChecker
{
    public class DeepFreezeChecker
    {
        // testing and update
        //Import DLL's (Dynamic Linked Libraries); these are needed for the following Method(s) to function
        [DllImport("user32.dll")]
        static extern int GetWindowText(IntPtr hWnd, StringBuilder text, int count);

        [DllImport("user32.dll", SetLastError = true)]
        static extern IntPtr FindWindow(string lpClassName, string lpWindowName);

        [DllImport("user32.dll")]
        static extern int SendMessage(IntPtr hWnd, uint msg, int wParam, int lParam);

        public const int WM_SYSCOMMAND = 0x0112;
        public const int SC_CLOSE = 0xF060;
        
        //Finds and Closes the Window of the passed parameter: dfWindow
        public static void FindAndCloseActiveWindow(string dfWindow)
        {
            const int charLength = 256;
            StringBuilder windowHeader = new StringBuilder(charLength);
            IntPtr findWin = FindWindow(null, dfWindow);

            //Get dfWindow
            GetWindowText(findWin, windowHeader, charLength);
            //Close dfWindow
            if (windowHeader.ToString() == dfWindow)
            {
                SendMessage(findWin, WM_SYSCOMMAND, SC_CLOSE, 0);
            }
        }

        //Main Function
        public static void Main(string[] args)
        {
            //Defining Variables
            var dateTime = DateTime.Now;
            string filePath = @" T:\Results.csv";
            string pass = "DeepFreeze Access," + dateTime + ",Pass" + Environment.NewLine;
            string fail = "DeepFreeze Access," + dateTime + ",Fail" + Environment.NewLine;
            const int charLength = 256;
            const string dfWindow = "Deep Freeze Enterprise";
            StringBuilder windowHeader = new StringBuilder(charLength);
            
            //Send the Key Press: Control + Shift + Alt + (F6)
            SendKeys.SendWait("(^(+(%{F6})))");

            //Sleep for half-second to ensure system has time to respond
            Thread.Sleep(500);

            //Initiating Handle to control the dfWindow so we can then use Methods like GetWindowText();
            IntPtr dfHandle = FindWindow(null, dfWindow);
            
            //Using Handle to evaluate Header value
            GetWindowText(dfHandle, windowHeader, charLength);

            //Output Test Results to CSV if the Window Name is accurately reflecting Deep Freeze
            if (windowHeader.ToString() == dfWindow)
            {
                //Output results to CSV 
                File.AppendAllText(filePath, pass + Environment.NewLine);
            }
            else
            {
                //Output results to CSV
                File.AppendAllText(filePath, fail+ Environment.NewLine);
            }
            //Closing dfWindow
            FindAndCloseActiveWindow(dfWindow);
            //Exit Application
            Application.Exit();
        }
    }
}

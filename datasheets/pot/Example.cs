    public class Program
    {
        public static void Main()
        {
            // For ChipWorkX
            MCP4131 myMCP4131 = new MCP4131(ChipworkX.Pin.PB7, SPI.SPI_module.SPI2);

            // For FEZ (Panda2)
            //MCP4131 myMCP4131 = new MCP4131((Cpu.Pin)FEZ_Pin.Digital.Di51, SPI.SPI_module.SPI2);

            myMCP4131.initTCON();
            Thread.Sleep(100);

            while (true)
            {
                myMCP4131.setTap(128);
                for (int i = 128; i > 0; i--)
                {
                    //myMCP4131.decrement();
                    myMCP4131.setTap(i); // Comment this line and use decrement above
                    Debug.Print("i=" + i);
                    myMCP4131.readTap();
                    Debug.Print("Wiper REG: " + myMCP4131.Wiper_Reg);
                    myMCP4131.readStatus();
                    Debug.Print("Status REG: " + myMCP4131.Status_Reg);
                    myMCP4131.readTCON();
                    Debug.Print("TCON: " + myMCP4131.Tcon_Reg);

                    Thread.Sleep(100);
                }
                Debug.Print("At zero");
                Thread.Sleep(5000);
                
                for (int i = 0; i < 128; i++)
                {
                    //myMCP4131.increment();
                    myMCP4131.setTap(i); // Comment this line and use increment above
                    Debug.Print("i=" + i);
                    myMCP4131.readTap();
                    Debug.Print("Wiper REG: " + myMCP4131.Wiper_Reg);
                    myMCP4131.readStatus();
                    Debug.Print("Status REG: " + myMCP4131.Status_Reg);
                    myMCP4131.readTCON();
                    Debug.Print("TCON: " + myMCP4131.Tcon_Reg);
                    Thread.Sleep(100);
                }
            }
        }
    }
